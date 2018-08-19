#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/8/1 17:59
# @Author   : z_jian
# @contact  : zjian1425@gmail.com
# @File     : get.py

import pymysql

def geturl(flag):
    conn = pymysql.connect('183.129.168.211', 'hexi', 'hexi123', 'db_ecommerce', charset='utf8')
    cursor = conn.cursor()

    do_select = '''select com_url from jd_url'''
    cursor.execute(do_select)

    if flag==0:

        url = cursor.fetchone()

        conn.commit()
        cursor.close()
        conn.close()

        return str(url[0])

    elif flag==1:

        url_list = []

        urls=cursor.fetchall()
        for i in urls:
            url_list.append(str(i[0]) )

        conn.commit()
        cursor.close()
        conn.close()

        return url_list