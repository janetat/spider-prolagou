"""
    @__author__: allen
    @__date__: 2018-8-27
    @__mission__: 爬取大鲲
    @__demand__: 项目名 + 发布日期 + 发布人 + 项目状态 + 详情 + 抓取时间
"""

import scrapy
import datetime
from spider_prolagou.items import SpiderProlagouItem

class ProLagouSpider(scrapy.Spider):
    name = 'pro_lagou'

    start_urls = [
        'https://pro.lagou.com/project/'
    ]

    def parse(self, response):
        # 爬取每个页面的项目
        for href in response.css('#project_list > ul > li > a::attr(href)'):
            yield response.follow(href, self.parse_project)

        base_url = self.start_urls[0]
        # 递归爬取分页的项目
        for i in range(1, 101):
            # 拼接成目标页面的url
            new_url = base_url + str(i)
            yield response.follow(new_url, self.parse)


    def parse_project(self, response):
        """爬取具体项目的信息
        :param response:
        :return:
        """

        def extract_with_css(query):
            return response.css(query).extract_first().strip()

        def extract_with_xpath(query):
            return response.xpath(query).extract_first().strip()

        item = SpiderProlagouItem()
        item['project_name'] = extract_with_css('.icon-bookmark + .project_key + span::text')
        item['pub_name'] = extract_with_css('.icon-building + .project_key + span::text')
        item['pub_time'] = extract_with_css('.icon-time + .project_key + span::text')
        item['project_status'] = extract_with_css('.status::text')
        item['project_detail'] = extract_with_css('.project_txt pre::text')
        item['current_time'] = datetime.datetime.now()

        yield {
            '项目名': item['project_name'] if item['project_name'] else None,
            '发布人': item['pub_name'] if item['pub_name'] else None,
            '发布时间': item['pub_time'] if item['pub_time'] else None,
            '项目状态': item['project_status'] if item['project_status'] else None,
            '详情': item['project_detail'] if item['project_detail'] else None,
            '抓取时间': item['current_time'],
        }