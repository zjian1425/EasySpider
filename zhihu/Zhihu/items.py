# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class ZhihuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    u_name = scrapy.Field()
    follwingCount = scrapy.Field()
    followerCount = scrapy.Field()
    gender = scrapy.Field()
    edu = scrapy.Field()
    job = scrapy.Field()
    place = scrapy.Field()
    url_token = scrapy.Field()
    asks = scrapy.Field()
    answerCount = scrapy.Field()
    introduce = scrapy.Field()


