# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from sqlalchemy.orm import sessionmaker

from amazon.models import Review, create_table, db_connect


class SQLitePipeline:
    def __init__(self):
        """
        Initializes database connection and sessionmaker
        Creates tables
        """
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """Save reviews in the database"""

        session = self.Session()
        review = Review()

        review.product_name = item["product_name"]
        review.asin = item["asin"]
        review.rating = item["rating"]
        review.reviewer = item["reviewer"]
        review.summary = item["summary"]
        review.review = item["review"]
        review.spider_name = item["spider"]
        review.scraping_date = item["scraping_date"]

        try:
            session.add(review)
            session.commit()

        except:
            session.rollback()
            raise

        finally:
            session.close()

        return item
