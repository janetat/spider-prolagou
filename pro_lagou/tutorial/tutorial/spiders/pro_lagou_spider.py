"""
    @__author__: allen
    @__date__: 2018-8-27
    @__mission__: 爬取大鲲
    @__demand__: 项目名 + 发布日期 + 发布人 + 项目状态 + 详情 + 抓取时间
"""

import scrapy
import datetime

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

        project_name = extract_with_css('.icon-bookmark + .project_key + span::text')
        pub_name = extract_with_css('.icon-building + .project_key + span::text')
        pub_time = extract_with_css('.icon-time + .project_key + span::text')
        project_status = extract_with_css('.status::text')
        project_detail = extract_with_css('.project_txt pre::text')
        current_time = datetime.datetime.now()

        yield {
            '项目名': project_name if project_name else None,
            '发布人': pub_name if project_name else None,
            '发布时间': pub_time if project_name else None,
            '项目状态': project_status if project_name else None,
            '详情': project_detail if project_name else None,
            '抓取时间': current_time,
        }