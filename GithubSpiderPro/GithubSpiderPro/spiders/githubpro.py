from ast import Num
import re
import scrapy
from scrapy import Selector, Request


class GithubproSpider(scrapy.Spider):
    name = 'githubpro'
    allowed_domains = ['github.com']
    start_urls = [f"https://github.com/topics/python?page={x}" for x in range(1, 2)]

    def parse(self, response):
        for article in response.xpath('//article'):
            user, proj = article.xpath('.//h3/a')
            item = {
                "user": user.xpath('./text()').get().strip(),
                "project": proj.xpath('./text()').get().strip()
            }
            # yield response.follow(
            #     proj.xpath('./@href').get(),
            #     callback=self.parse_repo,
            #     cb_kwargs=dict(basic_info=item)
            # )
            yield Request(
                url='https://github.com'+proj.xpath('./@href').get()+'/issues',
                callback=self.parse_issues,
                cb_kwargs=dict(basic_info=item),
                # dont_filter=True,
            )

    def parse_issues(self, response, basic_info):
        # num_str = response.xpath('//span[@id="issues-repo-tab-count"]/@title').get()
        # issues = ''.join(re.findall("\d+", num_str))
        # basic_info.update({'issues': int(issues)})

        num_str_list = response.xpath('.//div[@aria-live="polite"]/a[1]/text()').getall()
        num_str = '0'
        print(num_str_list)
        print('*'*50)
        for num in num_str_list:
            if num.strip():
                num_str = num.strip()
                break
        open_issues = ''.join(re.findall("\d+", num_str))

        num_str_list = response.xpath('.//div[@aria-live="polite"]/a[2]/text()').getall()
        num_str = '0'
        print(num_str_list)
        print('*'*50)
        for num in num_str_list:
            if num.strip():
                num_str = num.strip()
                break
        closed_issues = ''.join(re.findall("\d+", num_str))

        num_str = response.xpath('.//span[@id="repo-network-counter"]/@title').get()
        forks = ''.join(re.findall("\d+", num_str))

        basic_info.update({
            'open_issues': open_issues,
            'closed_issues':closed_issues,
            'forks':forks,
        })

        yield basic_info