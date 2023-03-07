# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GithubspiderItem(scrapy.Item):
    username = scrapy.Field()
    projname = scrapy.Field()
    userurl = scrapy.Field()
    projurl = scrapy.Field()
    star = scrapy.Field()
    about = scrapy.Field()
    topics = scrapy.Field()
    update = scrapy.Field()
