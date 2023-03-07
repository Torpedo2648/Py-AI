# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GithubspiderproItem(scrapy.Item):
    user = scrapy.Field()
    project = scrapy.Field()
    open_issues = scrapy.Field()
    closed_issues = scrapy.Field()
    forks = scrapy.Field()
