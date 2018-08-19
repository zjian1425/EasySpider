#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/6/21 16:12
# @Author   : z_jian
# @contact  : zjian1425@gmail.com
# @File     : Get_URL_from_mysql.py

import pymysql
import sys

def get(flag,spider_name):
    conn = pymysql.connect('IP','NAME','PASSWD','DB_NAME',charset='utf8')
    cursor = conn.cursor()

    if flag==0:
        do_select = '''select com_id from commodity_id where shop_name="{0}"'''.format(spider_name)
        cursor.execute(do_select)
        id= cursor.fetchone()
        if id:
            url = 'https://detail.tmall.com/item.htm?id='+str(id[0])+'&sku_properties=20509:28383'
            return url
        else:
            print('empty!!!')
            return None

    elif flag==1:
        do_select = '''select com_id from commodity_id where shop_name="{0}"'''.format(spider_name)
        cursor.execute(do_select)
        ids = cursor.fetchall()
        if ids:
            list = []
            for i in ids:
                list.append(str(i[0]))
            return list
        else:
            print('empty!!!')
            return None

    else:
        sys.exit('flag is wrong,only 0 or 1\n')



