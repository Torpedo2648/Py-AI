import scrapy
from scrapy import Selector, Request
from DoubanSpider.items import DoubanspiderItem


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']

    def start_requests(self):
        for page in range(10):
            yield Request(url=f'https://movie.douban.com/top250?start={page*25}&filter=')

    def parse(self, response):
        sel = Selector(response)
        item_list = sel.css('#content > div > div.article > ol > li')
        for item in item_list:
            movie_item = DoubanspiderItem()
            movie_item['title'] = item.css('span.title::text').get()
            movie_item['rank'] = item.css('span.rating_num::text').get()
            movie_item['subject'] = item.css('span.inq::text').get()
            yield movie_item
