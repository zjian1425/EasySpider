# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JdCommentsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    com_url = scrapy.Field()
    tag_string = scrapy.Field()
    content = scrapy.Field()
    creation_time = scrapy.Field()
    useful_vote_count = scrapy.Field()
    useless_vote_count = scrapy.Field()
    score = scrapy.Field()
    product_color = scrapy.Field()
    product_size = scrapy.Field()
    user_level_name = scrapy.Field()
    user_client_show = scrapy.Field()
    shop_name = scrapy.Field()
