#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : PeaceBird.py
# @Author: zjian
# @Date  : 18-7-27
# @Contact  :zjian1425@gmail.com 
#@Software : PyCharm


import scrapy
from scrapy.http import Request
from selenium import webdriver
from AimShopSpider_Detail.items import AimshopspiderDetailItem
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
from AimShopSpider_Detail.Get_URL_from_mysql import get
import sys

class PeaceBird(scrapy.Spider):

    name ='PeaceBird'
    allowed_domains = ['tmall.com']
    start_urls = []
    begin =  get(0,name)
    if begin:
        start_urls.append(begin)
    else:
        sys.exit('Missing start url')


    def __init__(self):
        '''params setting'''
        options = webdriver.ChromeOptions()
        prefs = {
            'profile.default_content_setting_values':{
                'images':2 #not allowed loading images
            }
        }
        options.add_experimental_option('prefs',prefs)
        # chrome_options = options
        self.driver = webdriver.Chrome()
        super(PeaceBird,self).__init__()
        dispatcher.connect(self.CloseSpider,signals.spider_closed)


    def  CloseSpider(self,spider):
            print('spiderClosed')
            self.driver.quit()


    def parse(self, response):
        for id in get(1,self.name):
            if id:
                url = 'https://detail.tmall.com/item.htm?id='+id
                yield  Request(url=url,meta={'id':id},callback=self.parse_detail)
            else:
                sys.exit('system waiting close')


    def parse_detail(self,response):

        '''extract field by CSS Selector'''
        title = response.css("div.tb-detail-hd h1::text").extract_first()
        title = "".join(title.split())
        o_price = response.css('#J_StrPriceModBox span::text').extract_first()
        n_price = response.css('div.tm-promo-price span::text').extract_first()
        sale_nums = response.css('li[class*=tm-ind-sellCount] span.tm-count::text').extract_first()
        comment_nums = response.css('#J_ItemRates span.tm-count::text').extract_first()
        fav_nums = response.css('#J_CollectCount::text').extract_first()
        product_params = response.css('#J_AttrUL li::text').extract()
        com_id = response.meta['id']

        '''define item object'''
        item = AimshopspiderDetailItem()
        item['com_id'] = com_id                 #商品id
        item['title'] =title                    #  商品标题
        item['o_price'] = o_price                   # 原价
        item['n_price'] = n_price                   # 促销价
        item['sale_nums'] = sale_nums           # 月销量
        item['comment_nums'] = comment_nums             # 累计评论数量
        item['fav_nums'] = fav_nums                     #收藏人数
        item['product_params'] = product_params         #产品参数
        yield item  #迭代返回