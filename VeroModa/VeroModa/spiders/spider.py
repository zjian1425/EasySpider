#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : spider.py
# @Author: zjian
# @Date  : 18-8-23
# @Contact  :zjian1425@gmail.com 
#@Software : PyCharm

import scrapy
from scrapy.http import Request
from selenium import webdriver
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
import re
import pymysql

class VM(scrapy.Spider):
    name = 'VM'
    allowed_domains = ['tmall.com']
    start_urls = ['https://www.only.cn/']
    count = 0
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
        # chrome_options = opt
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        super(VM, self).__init__()
        # 向CloseSpider方法发送爬虫结束信号，准备关闭pthantomjs浏览器
        dispatcher.connect(self.CloseSpider, signals.spider_closed)
        self.conn = pymysql.connect('','','','',charset = 'utf8')
        self.cursor = self.conn.cursor()
    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def CloseSpider(self, spider):
        print("spider closed")
        # 当爬虫结束时关闭浏览器
        self.driver.quit()

    def parse(self, response):
        #直接解析出商品url
        list = []
        li_list = response.css('#goodsListBox li a:nth-child(3)')
        for li in li_list:
            list.append(li.css('a::attr(href)').extract_first())


        for url in list:
            url='https://www.only.cn/'+str(url)
            yield Request(url=url,callback=self.parse_detail)
    def parse_detail(self,response):
        title = response.css('h3 span[class*="goods-name"]::text').extract_first()
        goods_num = response.css('p[class*="goods-num"] span::text').extract_first()
        n_price = response.css('strong.prices::text').extract_first()
        o_price = response.css('span.originalPrice::text').extract_first()
        color = ','.join(response.css('ul#colors li::text').extract())
        materials = response.css('#goods-infos::text').extract_first()

        pass
