#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File     : LeTin.py
# @Author   : Zjian
# @Time     : 18-7-23
# @Contact  :zjian1425@gmail.com
#@Software  : PyCharm

import scrapy
from scrapy.http import Request
from AimShopSpider_Comments.GetID import GetCommodityID
from AimShopSpider_Comments.GetID import GetCommentsUrl
from AimShopSpider_Comments.items import AimshopspiderCommentsItem
import re
import json
import datetime


class LeTing(scrapy.Spider):
    name = 'LeTin'
    allowed_domains = ['tmall.com']
    start_urls = GetCommentsUrl(GetCommodityID(0,spidername=name),spidername=name)+'1'

    def parse(self, response):
        for url in GetCommentsUrl(GetCommodityID(1, spidername=self.name), spidername=self.name):
            url = url + '1'
            # 在这里就进行翻页操作
            yield Request(url=url, callback=self.parse_detail, meta={'url': url})

    def parse_detail(self, response):

        # 提取商品ID
        GetId = lambda: re.match('.*?itemId=(\d.*)&.*?', response.meta['url']).group(1)
        com_id = int(GetId())
        # parse
        '''yield item'''
        jsoncontent = re.search('^[^(]*?\((.*)\)[^)]*$', response.text).group(1)
        jsdict = json.loads(jsoncontent)
        if jsdict['rateDetail']['rateList']:
            for i in jsdict['rateDetail']['rateList']:
                '''extract_field'''
                auctionSku = i['auctionSku']
                rateContent = i['rateContent']
                reply = i['reply']
                rateDate = i['rateDate']
                tradeEndTime = i['tradeEndTime']
                crawls_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # time formatting
                '''callback_storefunc'''
                item = AimshopspiderCommentsItem()
                item['auctionSku'] = auctionSku
                item['rateContent'] = rateContent
                item['reply'] = reply
                item['rateDate'] = rateDate
                item['tradeEndTime'] = tradeEndTime
                item['com_id'] = com_id
                item['tablename'] = self.name
                item['crawls_time'] = crawls_time
                yield item  # 迭代返回

        '''yield request'''
        '''以下代码实现单个商品评论页url翻页功能'''
        # 从url中提取出当前页码
        page_numsc = lambda: re.match('.*currentPage=(\d.*)', response.meta['url']).group(1)
        currentPage = int(page_numsc())
        # 末页
        page_numsl = lambda: re.match('.*"lastPage":(\d.*)', response.text).group(1)
        lastPage = int(page_numsl())

        # BaseURL
        BASE = lambda: re.match('（.*currentPage=）\d.*', response.meta['url']).group(1)
        if currentPage < lastPage:
            currentPage += 1
            url = BASE() + str(currentPage)
            yield scrapy.Request(url=url, callback=self.parse_detail, meta={'url': url})
