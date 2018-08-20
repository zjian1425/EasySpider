#! /usr/bin/env python
# -*- coding:utf-8 -*-
#@File  :girdear.PY
#@Author:zjian
#@Date :2018/8/7
#@contact :zjian1425@gmail.com
#@Software :PyCharm

import scrapy
from jd_commoditydetail.get import geturl
from scrapy.http import Request
from jd_commoditydetail.items import JdCommoditydetailItem
import requests
import re
import sys
import time
import json
from jd_commoditydetail.Random_func import Random_Headers
from jd_commoditydetail.Random_func import Random_Cookies
from selenium import webdriver
from scrapy import  signals
from scrapy.xlib.pydispatch import dispatcher


class girdear(scrapy.Spider):

    name='girdear'
    allowed_domains=['jd.com']
    start_urls = [str(geturl(0,name))]
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

        self.driver = webdriver.Chrome(chrome_options=opt)
        self.driver.implicitly_wait(10)
        super(girdear, self).__init__()
        # 向CloseSpider方法发送爬虫结束信号，准备关闭pthantomjs浏览器
        dispatcher.connect(self.CloseSpider, signals.spider_closed)

    def CloseSpider(self, spider):
        print("spider closed")
        # 当爬虫结束时关闭浏览器
        self.driver.quit()

    def parse(self, response):
        url_list = geturl(1,self.name)
        for i in url_list:
            yield Request(url=i,meta={'url':i},callback=self.parse_detail)

    def parse_detail(self,response):

        com_url = response.meta['url']
        title = response.css('div.sku-name::text').extract_first()
        n_price = response.css('span.p-price span:nth-child(2)::text').extract_first()
        o_price = response.css('#page_dpprice::text').extract_first()
        product_params = str(response.css('div.p-parameter ul:nth-child(2) li::text').extract())


        #单独js网址发起请求
        match_re = re.match('.*?/(\d*).html',com_url)
        id =''
        if match_re:
            id = match_re.group(1)
        else:
            print('正则提取商品id出错')
        #时间戳获取
        current_milli_time = lambda: int(round(time.time() * 1000))
        json_url = 'https://club.jd.com/comment/productCommentSummaries.action?referenceIds={0}&callback=json&_={1}'.format(id,current_milli_time())
        headers = Random_Headers(id)
        cookies = Random_Cookies()

        while True:
            r = requests.get(url=json_url,headers=headers,cookies=cookies)
            if r.status_code>=200 and r.status_code<300:
                break
            else:
                time.sleep(300)
                continue

        jscontent = re.search('^[^(]*?\((.*)\)[^)]*$',r.text).group(1)
        jsdict = json.loads(jscontent)

        comment_nums = jsdict['CommentsCount'][0]['CommentCountStr']
        good = jsdict['CommentsCount'][0]['GoodCountStr']
        good_rate = jsdict['CommentsCount'][0]['GoodRate']
        general = jsdict['CommentsCount'][0]['GeneralCountStr']
        general_rate = jsdict['CommentsCount'][0]['GeneralRate']
        poor = jsdict['CommentsCount'][0]['PoorCountStr']
        poor_rate = jsdict['CommentsCount'][0]['PoorCount']
        average_score = jsdict['CommentsCount'][0]['AverageScore']
        DefaultGoodCount = jsdict['CommentsCount'][0]['DefaultGoodCountStr']

        item = JdCommoditydetailItem()
        item['title'] = title
        item['n_price'] = n_price
        item['o_price'] = o_price
        item['comment_nums'] = comment_nums
        item['product_params'] = product_params
        item['shop_name'] = self.name
        item['good_rate'] = good_rate
        item['general_rate'] = general_rate
        item['com_url'] = com_url
        item['good'] = good
        item['general'] = general
        item['poor'] = poor
        item['poor_rate'] = poor_rate
        item['average_score'] = average_score
        item['DefaultGoodCount'] = DefaultGoodCount

        yield item