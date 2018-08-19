# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JdCommoditydetailItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    n_price = scrapy.Field()
    o_price = scrapy.Field()
    comment_nums = scrapy.Field()
    product_params = scrapy.Field()
    shop_name = scrapy.Field()
    fav_rate = scrapy.Field()
    tag = scrapy.Field()
    com_url = scrapy.Field()
    good = scrapy.Field()
    mid = scrapy.Field()
    bad = scrapy.Field()
    po_tu = scrapy.Field()
    pass
