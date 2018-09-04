#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Setting.py
# @Author: zjian
# @Date  : 18-9-3
# @Contact  :zjian1425@gmail.com 
#@Software : PyCharm

DB_info = {
    'host':'localhost',
    'username':'root',
    'password':'123456',
    'db_name':'db_ecommerce'
}
key = 'key=f163c1c6231cefbc845b910ac09901e7'
params = '&address='
BaseUrl = 'https://restapi.amap.com/v3/geocode/geo?'+key+params

do_select_sql = '''select distinct 收货地址 from gm_订单报表 where 订单创建时间<"2018-06-01"'''


# 3a6cc161062413a8381b085170d49d93

# select distinct 收货地址 from sensu_订单报表
# '''select distinct 收货地址 from av_订单报表 where 订单创建时间 < "2017-09-01"
#             union
#             select distinct 收货地址 from gm_订单报表 where 订单创建时间 < "2017-09-01"
#             union
#             select distinct 收货地址 from sensu_订单报表 where 订单创建时间 < "2017-09-01"'''