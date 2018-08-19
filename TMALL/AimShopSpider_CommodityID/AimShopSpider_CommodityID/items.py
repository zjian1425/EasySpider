# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AimshopspiderCommodityidItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    com_id_list = scrapy.Field() #商品id列表
    shop_name = scrapy.Field() #店铺名称