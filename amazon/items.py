# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ReviewItem(scrapy.Item):
    # Review Info
    product_name = scrapy.Field()
    asin = scrapy.Field()
    rating = scrapy.Field()
    reviewer = scrapy.Field()
    summary = scrapy.Field()
    review = scrapy.Field()

    # Spider info
    spider = scrapy.Field()
    scraping_date = scrapy.Field()
