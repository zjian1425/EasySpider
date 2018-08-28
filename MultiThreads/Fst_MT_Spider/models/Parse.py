#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Parse.py
# @Author: zjian
# @Date  : 18-8-25
# @Contact  :zjian1425@gmail.com 
#@Software : PyCharm



__doc__ = '''页面解析函数,返回迭代器'''


def parse(response):

    title = ''.join(response.css('h1.product_name::text').extract()).strip()
    bd = response.css('.product_name em::text').extract_first()
    goods_nums = response.css('#goods_detail_1 ul li:nth-child(1) .code::text').extract_first()  # 商品货号
    o_price = response.css('#goods_detail_1 ul li:nth-child(1) del::text').extract_first()
    n_price = response.css('#goods_detail_1 ul li.li_relative em::text').extract_first()
    sale_count = response.css('#goods_detail_1 ul li:nth-child(3) span::text').extract_first()
    comment_nums = response.css('span.comment_num a::text').extract_first()
    score = response.css('em.star-on::attr(title)').extract_first()
    brand = response.css('li#J_attrBrandName::attr(title)').extract_first()
    c_size = response.css('#J_AttrUL li:nth-child(3)::text').extract_first().replace('\n', '').replace(' ', '').replace(
        '\xa0', ',')
    color = response.css('#J_AttrUL li:nth-child(4)::text').extract_first().replace('\n', '').replace(' ', '').replace(
        '\xa0', ',')


    item = {'title':title,
            'bd':bd,
            'goods_nums':goods_nums,
            'o_price':o_price,
            'n_price':n_price,
            'sale_count':sale_count,
            'comment_nums':comment_nums,
            'score':score,
            'brand':brand,
            'c_size':c_size,
            'color':color
            }

    yield item