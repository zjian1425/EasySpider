#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File     : Qimi_tag.py
# @Author   : Zjian
# @Time     : 18-7-25
# @Contact  :zjian1425@gmail.com
#@Software  : PyCharm


import scrapy
from scrapy.http import Request
from AimShopSpider_Comments.GetID import GetCommodityID
from AimShopSpider_Comments.GetID import GetFrequentWordsUrl
from AimShopSpider_Comments.items import AimshopspiderTagItem
import re
import json
import datetime


class HM(scrapy.Spider):
    name = 'Qimi_tag'
    allowed_domains = ['tmall.com']
    start_urls = GetFrequentWordsUrl(GetCommodityID(0, spidername=name))
    
    def parse(self, response):
        for url in GetFrequentWordsUrl(GetCommodityID(1, spidername=self.name)):
            # 在这里就进行翻页操作
            yield Request(url=url, callback=self.parse_detail, meta={'url': url})
    
    def parse_detail(self, response):
        
        crawls_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # time formatting
        # 提取商品ID
        GetId = lambda: re.match('.*?itemId=(\d.*)&.*?', response.meta['url']).group(1)
        com_id = int(GetId())
        # parse
        '''yield item'''
        jsoncontent = re.search('^[^(]*?\((.*)\)[^)]*$', response.text).group(1)
        jsdict = json.loads(jsoncontent)
        if jsdict['tags']['tagClouds']:
            for i in jsdict['tags']['tagClouds']:
                '''extract_field'''
                tag_count = i['count']
                posi = i['posi']
                tag = i['tag']
                weight = i['weight']
                id = i['id']
                '''callback_storefunc'''
                item = AimshopspiderTagItem()
                item['com_id'] = com_id  # 商品id
                item['tag'] = tag  # 标签
                item['posi'] = posi  # 好评为True，差评为False
                item['tag_count'] = tag_count  # 标签计数
                item['crawls_time'] = crawls_time  # 抓取时间
                item['weight'] = weight
                item['id'] = id
                yield item  # 迭代返回