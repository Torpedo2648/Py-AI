# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GithubspiderpromaxItem(scrapy.Item):
    username = scrapy.Field()
    projname = scrapy.Field()
    userurl = scrapy.Field()
    projurl = scrapy.Field()
    stars = scrapy.Field()
    about = scrapy.Field()
    topics = scrapy.Field()
    update = scrapy.Field()
    open_issues = scrapy.Field()
    closed_issues = scrapy.Field()
    forks = scrapy.Field()
    readme = scrapy.Field()
    release = scrapy.Field()
    contributors = scrapy.Field()
    languages = scrapy.Field()
    branches = scrapy.Field()
    open_pulls = scrapy.Field()
    closed_pulls = scrapy.Field()
    dependencies = scrapy.Field()