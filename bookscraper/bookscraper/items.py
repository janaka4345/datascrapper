# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class BookscraperTodoItem(scrapy.Item):
    userId = scrapy.Field()
    id = scrapy.Field()
    title = scrapy.Field()
    completed = scrapy.Field()


class BookscraperUserItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    name = scrapy.Field()
    username = scrapy.Field()
    email = scrapy.Field()
