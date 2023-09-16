from scrapy.utils.project import get_project_settings
from sqlalchemy import (Column, DateTime, Float, Integer, String, Text,
                        create_engine)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(get_project_settings().get("CONNECTION_STRING"))


def create_table(engine):
    Base.metadata.create_all(engine)


class Review(Base):
    __tablename__ = "review"

    id = Column(Integer, primary_key=True)
    product_name = Column("product_name", String)
    asin = Column("asin_code", String, unique=True)
    rating = Column("rating", Float)
    reviewer = Column("reviewer", String)
    summary = Column("summary", String)
    review = Column("review", Text)
    spider_name = Column("spider_name", String)
    scraping_date = Column("scraping_date", DateTime)
