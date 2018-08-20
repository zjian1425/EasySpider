# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# # @File     : LeTin.py
# # @Author   : Zjian
# # @Time     : 18-7-23
# # @Desc     :In haiming
# # @Contact  :zjian1425@gmail.com
# #@Software  : PyCharm
# import scrapy
# from scrapy.http import Request
# from selenium import webdriver
# from scrapy.xlib.pydispatch import dispatcher
# from scrapy import signals
# import re
# from AimShopSpider_CommodityID.items import AimshopspiderCommodityidItem
#
# """https://leting.tmall.com/"""
# """python + selenium + webdriver render(javascript)"""
# class LeTing(scrapy.Spider):
#     name = 'LeTin'
#     allowed_domains = ['tmall.com']
#     start_urls = ['https://leting.tmall.com/search.htm?&pageNo=1']
#
#     """generation"""
#
#     def __init__(self):
#         # 禁止加载图片，提升爬取速度
#         opt = webdriver.ChromeOptions()
#         prefs = {
#             'profile.default_content_setting_values': {
#                 'images': 2
#             }
#         }
#         opt.add_experimental_option('prefs', prefs)
#         # chrome_options = opt
#         self.driver = webdriver.Chrome()
#         self.driver.implicitly_wait(10)
#         super(LeTing, self).__init__()
#         # 向CloseSpider方法发送爬虫结束信号，准备关闭pthantomjs浏览器
#         dispatcher.connect(self.CloseSpider, signals.spider_closed)
#
#     def CloseSpider(self, spider):
#         print("spider closed")
#         # 当爬虫结束时关闭浏览器
#         self.driver.quit()
#
#     def parse(self, response):
#         for i in range(2,20):
#             url = 'https://leting.tmall.com/search.htm?&pageNo={0}'.format(i)
#             '''iteration  / generation'''
#             yield Request(url=url,callback=self.parse_detail)#注意这里调用不需要有()
#
#     def parse_detail(self,response):
#         '''use CSS Selector&REGEXP extract commodity_id'''
#
#         com_id_cluster = response.css('#J_ShopSearchResult img:nth-child(1)::attr(src)').extract_first()
#         com_id_list = []
#         print(com_id_cluster)
#         type(com_id_cluster)
#         list = re.finditer(r"(\d{12})%2C", com_id_cluster)
#         for i in list:
#             id = i.group(1)
#             com_id_list.append(id)
#
#         item = AimshopspiderCommodityidItem()
#         item['com_id_list'] = com_id_list
#         item['shop_name'] = self.name
#         yield item
#
