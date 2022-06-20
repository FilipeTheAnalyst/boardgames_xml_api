# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BoardgamesItem(scrapy.Item):
    # define the fields for your item here like:
    id = scrapy.Field()
    rank = scrapy.Field()
    name = scrapy.Field()
    url = scrapy.Field()
    rating = scrapy.Field()
    num_voters = scrapy.Field()
    year = scrapy.Field()
    details = scrapy.Field()
    date = scrapy.Field()
