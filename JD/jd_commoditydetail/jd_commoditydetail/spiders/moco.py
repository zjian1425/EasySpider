#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/8/1 16:35
# @Author   : z_jian
# @contact  : zjian1425@gmail.com
# @File     : moco.py


import scrapy
from jd_commoditydetail.get import geturl
from scrapy.http import Request
from jd_commoditydetail.items import JdCommoditydetailItem
from selenium import webdriver
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals


class moco(scrapy.Spider):

    name='moco'
    allowed_domains=['jd.com']
    start_urls = [str(geturl(0))]



    """generation"""

    def __init__(self):
        # 禁止加载图片，提升爬取速度
        opt = webdriver.ChromeOptions()
        prefs = {
            'profile.default_content_setting_values': {
                'images': 2
            }
        }
        opt.add_experimental_option('prefs', prefs)

        self.driver = webdriver.Chrome(chrome_options = opt)
        self.driver.implicitly_wait(10)
        super(moco, self).__init__()
        # 向CloseSpider方法发送爬虫结束信号，准备关闭pthantomjs浏览器
        dispatcher.connect(self.CloseSpider, signals.spider_closed)

    def CloseSpider(self, spider):
        print("spider closed")
        # 当爬虫结束时关闭浏览器
        self.driver.quit()


    def parse(self, response):
        url_list = geturl(1)
        for i in url_list:
            yield Request(url=i,meta={'url':i},callback=self.parse_detail)

    def parse_detail(self,response):
        title = response.css('div.sku-name::text').extract_first()
        n_price = response.css('span.p-price span:nth-child(2)::text').extract_first()
        o_price = response.css('#page_dpprice::text').extract_first()
        comment_nums = response.css('div#comment-count a::text').extract_first()
        product_params = str(response.css('div.p-parameter ul:nth-child(2) li::text').extract())
        fav_rate = response.css('div.percent-con::text').extract_first()
        tag = str(response.css('div.percent-info span::text').extract())
        com_url = response.meta['url']
        good = response.css('li[clstag$="haoping"] em::text').extract_first()
        mid = response.css('li[clstag$="zhongping"] em::text').extract_first()
        bad = response.css('li[clstag$="chaping"] em::text').extract_first()
        po_tu = response.css('li[clstag$="shaidantab"] em::text').extract_first()


        item = JdCommoditydetailItem()
        item['title'] = title
        item['n_price'] = n_price
        item['o_price'] = o_price
        item['comment_nums'] = comment_nums
        item['product_params'] = product_params
        item['shop_name'] = self.name
        item['fav_rate'] = fav_rate
        item['tag'] = tag
        item['com_url'] = com_url
        item['good'] = good
        item['mid'] = mid
        item['bad'] = bad
        item['po_tu'] = po_tu
        yield item