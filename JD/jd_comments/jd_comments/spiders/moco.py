# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# # @Time     : 2018/8/3 11:17
# # @Author   : z_jian
# # @contact  : zjian1425@gmail.com
# # @File     : moco.py
#
# import scrapy
# from jd_comments.getIDfrom_url import UrlJoin
# from scrapy.http import Request
# from jd_comments.getIDfrom_url import GetPrimaryKey_url
# from time import ctime
# import re
# import json
# from jd_comments.items import JdCommentsItem
# from jd_comments.Random_func import Random_Headers
# from jd_comments.getIDfrom_url import Get_CurrentId
#
#
# class moco(scrapy.Spider):
#     name = 'moco'
#     allowed_domains = ['jd.com']
#     start_urls = [UrlJoin(0,name)]
#
#     def parse(self, response):
#
#         for request_url in UrlJoin(1,self.name):
#             #控制切换url
#             yield Request(url=request_url,meta={'current_url':GetPrimaryKey_url(request_url)},
#                               headers=Random_Headers(Get_CurrentId(request_url)),callback=self.parse_detail)
#
#         with open('running.log','a+') as f:
#             f.write('[%s] %s'%(ctime(),'crawled success!!!')+'\n')
#         f.close()
#
#     def parse_detail(self,response):
#
#         jscontent = re.search('^[^(]*?\((.*)\)[^)]*$', response.text).group(1)
#         jsdict = json.loads(jscontent)
#         '''define'''
#         tag_string = ''
#         content = ''
#         creation_time = ''
#         useful_vote_count = ''
#         useless_vote_count = ''
#         score = ''
#         product_color = ''
#         product_size = ''
#         user_level_name = ''
#         user_client_show = ''
#         shop_name = self.name
#
#         if jsdict['hotCommentTagStatistics']:
#             for i in jsdict['hotCommentTagStatistics']:
#                 tag_string = tag_string+i['name']+str(i['count'])+';'
#
#         com_url = response.meta['current_url']
#
#         if jsdict['comments']:
#                 for i in jsdict['comments']:
#                     content = i['content']
#                     creation_time = i['creationTime']
#                     useful_vote_count=i['usefulVoteCount']
#                     useless_vote_count = i['uselessVoteCount']
#                     score = i['score']
#                     product_color = i['productColor']
#                     product_size = i['productSize']
#                     user_level_name = i['userLevelName']
#                     user_client_show = i['userClientShow']
#
#                     item = JdCommentsItem()
#
#                     item['com_url'] = com_url
#                     item['tag_string'] = tag_string
#                     item['content'] = content
#                     item['creation_time'] = creation_time
#                     item['useful_vote_count'] = useful_vote_count
#                     item['useless_vote_count'] = useless_vote_count
#                     item['score'] = score
#                     item['product_color'] = product_color
#                     item['product_size'] = product_size
#                     item['user_level_name'] = user_level_name
#                     item['user_client_show'] = user_client_show
#                     item['shop_name'] = shop_name
#                     yield item
#
#                 pre = re.match('(.*?page=)\d+(.*?)',response.url).group(1)
#                 pos = re.match('(.*?page=)\d+(.*)',response.url).group(2)
#                 infix = str(int(re.match('.*?page=(\d+).*?',response.url).group(1)) + 10)
#
#                 #控制翻页
#                 yield Request(url=pre+infix+pos, meta={'current_url':com_url},
#                         headers=Random_Headers(Get_CurrentId(response.url)), callback=self.parse_detail)
#
#
#
#
