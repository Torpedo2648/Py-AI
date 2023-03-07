from queue import Empty
import scrapy
from scrapy import Selector
from GithubSpider.items import GithubspiderItem

class GithubSpider(scrapy.Spider):
    name = 'Github'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/topics/python?page='+ str(page) for page in range(1,11)]

    def parse(self, response):
        sel = Selector(response)
        proj_list = sel.css('article')
        for proj in proj_list:
            proj_item = GithubspiderItem()
            username, projname = proj.xpath('.//h3/a')
            proj_item['username'] = username.xpath('./text()').get().strip()
            proj_item['userurl'] = self.allowed_domains[0] + username.xpath('./@href').get().strip()
            proj_item['projname'] = projname.xpath('./text()').get().strip()
            proj_item['projurl'] = self.allowed_domains[0] + projname.xpath('./@href').get().strip()

            proj_item['star'] = proj.xpath('.//a/span[2]/@aria-label').get().split(' ')[0]
            
            about, topic, update = proj.xpath('./div[2]/div')
            emoji = about.xpath('./div/g-emoji/text()')
            if emoji:
                proj_item['about'] = emoji.get().strip() + about.xpath('./div/text()').get().strip()
            else:
                proj_item['about'] = about.xpath('./div/text()').get().strip()

            proj_item['topics'] = []
            topic_list = topic.xpath('./a')
            for topic_item in topic_list:
                proj_item['topics'].append(topic_item.xpath('./text()').get().strip())
            proj_item['update'] = update.xpath('.//relative-time/text()').get().strip()

            yield proj_item