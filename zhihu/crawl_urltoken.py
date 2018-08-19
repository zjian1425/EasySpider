#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/4/10 19:00
# @Author   : z_jian
# @contact  : zjian1425@gmail.com
# @File     : crawl_urltoken.py

from Zhihu.All_method import add_url_token
import pymysql

# operate_mysql()
ch = input("Enter first url_token:")
add_url_token(ch)  # 获取初始用户关注的所有用户url_token函数,插入数据库表urltoken中
conn = pymysql.connect("localhost", "username", "password", "db_name", charset="utf8")
cursor = conn.cursor()
do_select = """select url_token from url_token_test"""
# 执行查询动作
cursor.execute(do_select)
i = 0
while True:
    # 获取当前游标指向第一行数据
    url_token = cursor.fetchone() #tuple值，需要转换成str
    if url_token:
        add_url_token("".join(url_token))
        cursor.nextset()
        conn.commit()
        i = i + 1
    else:
        print("表空")
        break
#关闭游标
cursor.close()

#关闭连接
conn.close()