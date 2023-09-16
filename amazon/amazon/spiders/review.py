import random
from datetime import datetime
from urllib.parse import quote_plus, urlencode, urljoin

import scrapy
from scrapy_splash import SplashRequest

from amazon.itemloaders import ReviewLoader
from amazon.items import ReviewItem
from amazon.user_agent_and_proxy_lists import proxies_list, user_agent_list

queries = ["skin care"]


class ReviewSpider(scrapy.Spider):
    name = "amazon_review"
    custom_settings = {
        "AUTOTHROTTLE_ENABLED": True,
        "AUTOTHROTTLE_DEBUG": True,
    }

    def start_requests(self):
        for query in queries:
            url = f"https://www.amazon.com/s?k={quote_plus(query)}"
            yield SplashRequest(url=url, callback=self.parse_products_list)

    def parse_products_list(self, response):
        # Get all asin codes in the page
        asin_list = response.xpath("//@data-asin").getall()
        # Clean and filter codes
        asin_list = [i for a, i in enumerate(asin_list) if i != ""]

        for asin in asin_list:
            review_url = f"https://www.amazon.com/product-reviews/{asin}"
            yield SplashRequest(
                url=review_url, callback=self.parse_reviews, meta={"asin_code": asin}
            )

        next_page = response.xpath("//a[contains(text(), Next)]/@href").get()
        if next_page:
            url = urljoin("https://www.amazon.com", next_page)
            yield SplashRequest(url=url, callback=self.parse_products_list)

    def parse_reviews(self, response):
        asin_code = response.meta["asin_code"]
        product_review = response.css("div#cm_cr-review_list")
        product_name = response.xpath(
            '//*[@id="cm_cr-product_info"]/div/div[2]/div/div/div[2]/div[1]/h1/a/text()'
        ).get()
        for data in product_review:
            review_info = ReviewLoader(item=ReviewItem(), selector=data)
            review_info.add_value("product_name", product_name)
            review_info.add_value("asin", asin_code)
            review_info.add_xpath(
                "rating", "//i[@data-hook='review-star-rating']/span/text()"
            )
            review_info.add_xpath("reviewer", "//span[@class='a-profile-name']/text()")
            review_info.add_xpath(
                "summary", "//a[@data-hook='review-title']/span[2]/text()"
            )
            review_info.add_xpath(
                "review", "//span[@data-hook='review-body']/span/text()"
            )

            review_info.add_value("spider", self.name)
            review_info.add_value("scraping_date", datetime.now())

            yield review_info.load_item()

        # next_page = response.xpath("//li[contains(@class, a-last)]/a/@href").get()
        # print('Parsing Page 2', next_page)
        # if next_page:
        #     url = 'https://www.amazon.com' + next_page
        #     yield SplashRequest(url=url, callback=self.parse_reviews,  meta={"asin_code": asin_code})
