from gc import callbacks
from sys import call_tracing
from telnetlib import SE
import scrapy
import pandas as pd
from scrapy import Selector
import QuoteSpider.items as qs

class QuoteSpider(scrapy.Spider):
    name = 'quote'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        quote_list = response.xpath('//div[@class="quote"]')
        for quote in quote_list:

            QuoteItem = qs.QuotespiderItem()

            text = quote.xpath('./span[1]/text()').get()[1:-1]
            author = quote.xpath('.//small[@class="author"]/text()').get()
            
            tags = []
            tags_list = quote.xpath('.//a[@class="tag"]')
            for tags_ in tags_list:
                tags.append(tags_.xpath('./text()').get())

            QuoteItem = dict(text=text, author=author, tags=tags)

            about_url = quote.xpath('./span[2]/a/@href').get()
            yield response.follow(
                about_url,
                callback=self.parse_author,
                cb_kwargs=dict(Item=QuoteItem),
                )

        nextpage_url = response.xpath('//li[@class="next"]/a/@href').get()
        if nextpage_url:
            yield response.follow(nextpage_url,callback=self.parse)

    def parse_author(self, response, Item):
        Item.update(
            {
                # 'name':response.xpath('//h3/text()').get().strip(),
                'born_date':response.xpath('//span[@class="author-born-date"]/text()').get(),
                'born_location':response.xpath('//span[@class="author-born-location"]/text()').get(),
                'desciption':response.xpath('//div[@class="author-description"]/text()').get().strip()[:100]
            }
        )
        yield Item