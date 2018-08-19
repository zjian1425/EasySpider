#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/8/1 13:08
# @Author   : z_jian
# @contact  : zjian1425@gmail.com
# @File     : moco.py


import scrapy
from scrapy.http import Request
from selenium import webdriver
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
import re
from jd_url.items import JdUrlItem

"""https://hm.tmall.com/"""
"""python + selenium + webdriver render(javascript)"""


class moco(scrapy.Spider):
    name = 'moco'
    allowed_domains = ['jd.com']
    start_urls = ['https://www.jd.com/']

    count = 1

    """generation"""

    def __init__(self):
        # 禁止加载图片，提升爬取速度
        opt = webdriver.ChromeOptions()
        prefs = {
            'profile.default_content_setting_values': {
                'images': 2
            }
        }
        opt.add_experimental_option('prefs', prefs)

        self.driver = webdriver.Chrome(chrome_options = opt)
        self.driver.implicitly_wait(10)
        super(moco, self).__init__()
        # 向CloseSpider方法发送爬虫结束信号，准备关闭pthantomjs浏览器
        dispatcher.connect(self.CloseSpider, signals.spider_closed)

    def CloseSpider(self, spider):
        print("spider closed")
        # 当爬虫结束时关闭浏览器
        self.driver.quit()

    def parse(self, response):
        for i in range(1,2):
            url = 'https://mall.jd.com/view_search-184757-0-5-1-24-{0}.html'.format(i)
            '''iteration  / generation'''
            yield Request(url=url, callback=self.parse_detail)  # 注意这里调用不需要有()

    def parse_detail(self, response):
        '''use CSS Selector&REGEXP extract commodity_id'''
        com_url_list = []
        cnt = 1
        while cnt<25:

            com_url = response.css('li.jSubObject:nth-child({0}) div.jItem div.jPic a::attr(href)'.format(cnt)).extract_first()
            if com_url:
                com_url = 'https:'+com_url
                com_url_list.append(com_url)
                cnt +=1
            else:
                break


        item = JdUrlItem()
        item['com_url_list'] = com_url_list
        item['shop_name'] = self.name
        yield item

