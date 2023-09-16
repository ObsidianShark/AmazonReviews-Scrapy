from itemloaders.processors import Identity, Join, MapCompose, TakeFirst
from scrapy.loader import ItemLoader


class ReviewLoader(ItemLoader):
    default_input_processor = MapCompose(str.strip, str.capitalize)
    default_output_processor = TakeFirst()

    asin_in = Identity()
    rating_in = MapCompose(lambda x: x.strip().split(" ")[0], float)
    scraping_date_in = MapCompose()
