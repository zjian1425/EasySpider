#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/8/3 11:40
# @Author   : z_jian
# @contact  : zjian1425@gmail.com
# @File     : getIDfrom_url.py


import pymysql

def geturl(flag,name):

    conn = pymysql.connect('183.129.168.211','hexi','hexi123','db_ecommerce',charset='utf8')
    cursor = conn.cursor()
    do_select = '''select com_url from jd_url where shop_name="{0}"'''.format(name)
    cursor.execute(do_select)

    if flag==0:
        url = (cursor.fetchone())[0]
        conn.commit()
        cursor.close()
        conn.close()
        return url
    elif flag==1:
        url_list=[]
        url_tuple = cursor.fetchall()
        for i in url_tuple: url_list.append(i[0])

        return url_list

import re


def getId(flag,name):

    if flag==0: return re.match('.*/(\d*).html',geturl(flag,name)).group(1)

    elif flag==1:
        id_list = []
        url_list = geturl(flag,name)
        for i in url_list:
            id_list.append(re.match('.*/(\d*).html',i).group(1))

        return id_list


#拼接评论url方法
def UrlJoin(flag,name):
    first_page_url='https://sclub.jd.com/comment/productPageComments.action?' \
                   'callback=json&score=0&sortType=5&page=0' \
                   '&pageSize=10&productId='

    if flag==0:return first_page_url+getId(flag,name)
    elif flag==1:

        c_url_list = []

        id_list = getId(flag,name)
        for i in  id_list:
            c_url_list.append(first_page_url+i)
        return c_url_list

import  sys

def GetPrimaryKey_url(comments_url):

    if comments_url and isinstance(comments_url,str):
        productId = re.match('.*?productId=(\d*).*?',comments_url).group(1)
        return 'https://item.jd.com/{0}.html'.format(productId)
    else:
        print('Error')


def Get_CurrentId(comments_url):

    if comments_url and isinstance(comments_url,str):
        productId = re.match('.*?productId=(\d*).*?',comments_url).group(1)
        return productId
    else:
        print('Error')