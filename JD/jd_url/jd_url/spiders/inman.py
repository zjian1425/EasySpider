#! /usr/bin/env python
# -*- coding:utf-8 -*-
#@File  :inman.PY
#@Author:zjian
#@Date :2018/8/6
#@contact :zjian1425@gmail.com
#@Software :PyCharm


import scrapy
from scrapy.http import Request
from selenium import webdriver
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
from jd_url.items import JdUrlItem

"""https://hm.tmall.com/"""
"""python + selenium + webdriver render(javascript)"""


class inman(scrapy.Spider):
    name = 'inman'
    allowed_domains = ['jd.com']
    start_urls = ['https://mall.jd.com/view_search-112147-37335-35324-0-0-0-0-1-1-60.html?keyword=VP']

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
        super(inman, self).__init__()
        # 向CloseSpider方法发送爬虫结束信号，准备关闭pthantomjs浏览器
        dispatcher.connect(self.CloseSpider, signals.spider_closed)

    def CloseSpider(self, spider):
        print("spider closed")
        # 当爬虫结束时关闭浏览器
        self.driver.quit()

    def parse(self, response):
        for i in range(2,30):
            url = 'https://mall.jd.com/view_search-112147-37335-35324-0-0-0-0-1-{0}-60.html?keyword=VP'.format(i)
            '''iteration  / generation'''
            yield Request(url=url, callback=self.parse_detail)

    def parse_detail(self, response):
        '''use CSS Selector&REGEXP extract commodity_id'''
        com_url_list = []
        cnt = 1
        while cnt<81:

            com_url = response.css('div.j-module li.jSubObject:nth-child({0}) div.jItem div.jPic a::attr(href)'.format(cnt)).extract_first()
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