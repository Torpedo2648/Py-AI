import re
import scrapy
from scrapy import Request
from GithubSpiderProMax.settings import COOKIES_DICT

class GithubpromaxSpider(scrapy.Spider):
    name = 'githubpromax'
    allowed_domains = ['github.com']
    start_urls = [f"https://github.com/topics/python?page={x}" for x in range(1, 51)]

    def parse(self, response):
        proj_list = response.xpath('//article')
        for proj in proj_list:
            basic_info = {}
            user, project = proj.xpath('.//h3/a')
            basic_info['username'] = user.xpath('./text()').get().strip()
            basic_info['userurl'] = 'https://' + self.allowed_domains[0] + user.xpath('./@href').get().strip()
            basic_info['projname'] = project.xpath('./text()').get().strip()
            basic_info['projurl'] = 'https://' + self.allowed_domains[0] + project.xpath('./@href').get().strip()

            basic_info['stars'] = int(proj.xpath('.//a/span[2]/@aria-label').get().split(' ')[0])
            
            about, topic, update = proj.xpath('./div[2]/div')
            emoji = about.xpath('./div/g-emoji/text()')
            if emoji:
                basic_info['about'] = emoji.get().strip() + about.xpath('./div/text()').get().strip()
            else:
                basic_info['about'] = about.xpath('./div/text()').get().strip()

            basic_info['topics'] = []
            topic_list = topic.xpath('./a')
            for topic_basic_info in topic_list:
                basic_info['topics'].append(topic_basic_info.xpath('./text()').get().strip())

            basic_info['update'] = update.xpath('.//relative-time/text()').get().strip()

            yield Request(
                url=basic_info['projurl'],
                callback=self.parse_repo,
                cb_kwargs=dict(basic_info=basic_info),
                cookies=COOKIES_DICT
            )

    def parse_repo(self, response, basic_info):

        num_str = response.xpath('.//span[@id="repo-network-counter"]/@title').get()
        forks = int(''.join(re.findall("\d+", num_str)))
        readme = basic_info['projurl']+'#readme'
        num_str = response.xpath('.//a[@class="Link--primary no-underline"]/span/@title').get()
        release = int(''.join(re.findall('\d+', num_str)))
        num_str = response.xpath('.//a[@class="Link--primary no-underline"]/span/@title').getall()[-1]
        contributors = int(''.join(re.findall('\d+', num_str)))
        num_str = response.xpath('.//a[@data-pjax="#repo-content-pjax-container"]/strong/text()').get()
        branches = int(''.join(re.findall('\d+', num_str)))

        langs = response.xpath('.//li[@class="d-inline"]/a/span[1]/text()').getall()
        percents = response.xpath('.//li[@class="d-inline"]/a/span[2]/text()').getall()
        languages = {}
        for lang, num_str in zip(langs, percents):
            percent = round(float(''.join(re.findall('[\d\.]+', num_str)))/100, 2)
            languages[lang] = percent

        basic_info.update({
            'forks':forks,
            'readme':readme,
            'release':release,
            'contributors':contributors,
            'languages':languages,
            'branches':branches,
        })
        yield Request(
            url=basic_info['projurl']+'/issues',
            callback=self.parse_issues,
            cb_kwargs=dict(basic_info=basic_info),
            cookies=COOKIES_DICT
        )

    def parse_issues(self, response, basic_info):

        num_str_list = response.xpath('.//div[@aria-live="polite"]/a[1]/text()').getall()
        num_str = '0'
        for num in num_str_list:
            if num.strip():
                num_str = num.strip()
                break
        open_issues = int(''.join(re.findall("\d+", num_str)))

        num_str_list = response.xpath('.//div[@aria-live="polite"]/a[2]/text()').getall()
        num_str = '0'
        for num in num_str_list:
            if num.strip():
                num_str = num.strip()
                break
        closed_issues = int(''.join(re.findall("\d+", num_str)))

        basic_info.update({
            'open_issues': open_issues,
            'closed_issues':closed_issues,
        })
        yield Request(
                url=basic_info['projurl']+'/pulls',
                callback=self.parse_pulls,
                cb_kwargs=dict(basic_info=basic_info),
                cookies=COOKIES_DICT
        )
    
    def parse_pulls(self, response, basic_info):

        num_str_list = response.xpath('.//div[@aria-live="polite"]/a[1]/text()').getall()
        num_str = '0'
        for num in num_str_list:
            if num.strip():
                num_str = num.strip()
                break
        open_pulls = int(''.join(re.findall("\d+", num_str)))

        num_str_list = response.xpath('.//div[@aria-live="polite"]/a[2]/text()').getall()
        num_str = '0'
        for num in num_str_list:
            if num.strip():
                num_str = num.strip()
                break
        closed_pulls = int(''.join(re.findall("\d+", num_str)))

        basic_info.update({
            'open_pulls': open_pulls,
            'closed_pulls':closed_pulls,
        })

        yield Request(
            url=basic_info['projurl']+'/network/dependencies',
            callback=self.parse_dependencies,
            cb_kwargs=dict(basic_info=basic_info),
            cookies=COOKIES_DICT
        )

    def parse_dependencies(self, response, basic_info):
        dependencies = response.xpath('.//a[@data-octo-click="dep_graph_package"]/@href').getall()
        basic_info.update({
            'dependencies': dependencies,
        })
        yield basic_info
