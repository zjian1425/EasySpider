#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test.py
# @Author: zjian
# @Date  : 18-9-3
# @Contact  :zjian1425@gmail.com 
#@Software : PyCharm
# import requests
# import json
#
# url = 'https://restapi.amap.com/v3/geocode/geo?key=ffa5934a02d3668aaca3cb570ca2ecf2&address=山东省 济南市 历下区 文化东路与山大路交叉口恒大帝景4号楼一楼商铺吴公洛口腔诊所(250013)'
# a = requests.get(url)
# b = a.content.decode('utf8')
# dic1 = json.loads(b)
# pass
# 山东省 济南市 历下区 文化东路与山大路交叉口恒大帝景4号楼一楼商铺吴公洛口腔诊所(250013)
# a = "116.480656,39.989677"
# c = a.split(',')
# x = a.split(',')[0]
# y = a.split(',')[1]
# # pass
#
import pymysql
from Setting import *
from queue import Queue

conn = pymysql.connect(DB_info['host'],DB_info['username'],DB_info['password'],
                                    DB_info['db_name'],charset='utf8')
cursor = conn.cursor()

do_select = '''select distinct 收货地址 from av_订单报表 where 订单创建时间 < "2017-09-01"
               union
               select distinct 收货地址 from gm_订单报表 where 订单创建时间 < "2017-09-01"
               union
               select distinct 收货地址 from ss_订单报表 where 订单创建时间 < "2017-09-01" '''
cursor.execute(do_select)
a = cursor.fetchall()
q = Queue(maxsize=300000)
for i in a:
    q.put(i[0])
pass


#
# class ls(object):
#
#     def __init__(self,name):
#         self.name = name
#
#     def __call__(self, *args, **kwargs):
#         self.run()
#     def run(self):
#         print(self.name)
#
#
# a = ls('sam')
# a.__call__()
# pass