# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

'''全部评论专用Item对象'''
class AimshopspiderCommentsItem(scrapy.Item):
    # define the fields for your item here like:
    auctionSku = scrapy.Field()
    rateContent = scrapy.Field()
    reply = scrapy.Field()
    rateDate = scrapy.Field()
    tradeEndTime = scrapy.Field()
    com_id = scrapy.Field()
    crawls_time = scrapy.Field()

'''标签词专用Item对象'''
class AimshopspiderTagItem(scrapy.Item):
    # define the fields for your item here like:
    com_id = scrapy.Field()
    tag = scrapy.Field()
    posi = scrapy.Field()
    tag_count = scrapy.Field()
    weight = scrapy.Field()
    index = scrapy.Field()
    crawls_time = scrapy.Field()