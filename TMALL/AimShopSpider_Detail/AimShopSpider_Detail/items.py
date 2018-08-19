# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AimshopspiderDetailItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    com_id =scrapy.Field()                                 #商品id
    title = scrapy.Field()                                #  商品标题
    o_price = scrapy.Field()                            # 原价
    n_price = scrapy.Field()                            #促销价
    sale_nums = scrapy.Field()                       # 月销量
    comment_nums = scrapy.Field()              # 累计评论数量
    fav_nums = scrapy.Field()                        #收藏人数
    product_params = scrapy.Field()                    #产品参数
