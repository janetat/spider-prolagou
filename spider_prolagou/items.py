# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderProlagouItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    project_name = scrapy.Field()
    pub_name = scrapy.Field()
    pub_time = scrapy.Field()
    project_status = scrapy.Field()
    project_detail = scrapy.Field()
    current_time = scrapy.Field()




"""
            '项目名': project_name if project_name else None,
            '发布人': pub_name if project_name else None,
            '发布时间': pub_time if project_name else None,
            '项目状态': project_status if project_name else None,
            '详情': project_detail if project_name else None,
            '抓取时间': current_time,
"""
