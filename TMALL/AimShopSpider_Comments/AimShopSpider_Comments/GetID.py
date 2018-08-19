#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File     : GetID.py
# @Author   : Zjian
# @Time     : 18-7-25
# @Desc     :In haiming
# @Contact  :zjian1425@gmail.com
#@Software  : PyCharm

import pymysql
import sys
import time

def GetCommodityID(flag,spidername):
    '''initialization'''
    conn = pymysql.connect('XXXXX','XXXX','XXXXX','XXXXX',charset='utf8')
    cursor = conn.cursor()
    
    if flag==0:
        '''获取起始商品url的id'''
        do_select = '''select com_id from {0}'''.format(spidername)
        cursor.execute(do_select)
        id= cursor.fetchone()
        if id:
            return str(id[0])
        else:
            print('empty!!!')
            return None
    elif flag==1:
        '''获取全部商品url的id'''
        do_select = '''select com_id from {0}'''.format(spidername)
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
        
        
def GetCommentsUrl(ID,spidername): # ID 可以是str，也可以是list
    
    sellerId= {'HM':'3676232520',
               'Hstyle':'263817957',
               'LeTin':'513051429',
               'Loytio':'2259671921',
               'Only':'356060330',
               'PeaceBird':'112394247',
               'Qimi':'1766047907',
               'Uniqlo':'196993935',
               'VeroModa':'420567757',
               'Zara':'2228361831'
               }
    
    baseURL = 'https://rate.tmall.com/list_detail_rate.htm?itemId='
    prams1 = '&sellerId='+sellerId[spidername]
    prams2 = '&callback=json'
    prams3 = '&currentPage='
    
    if isinstance(ID,str):
        return  baseURL+ID+prams1+prams2+prams3
    
    elif isinstance(ID,list):
        urls = []
        for id in ID:
            urls.append(baseURL+id+prams1+prams2+prams3)
        return urls   #list
    '''当前返回的都为商品评论页面第一页的url，翻页操作在调用函数中实现'''


def GetFrequentWordsUrl(ID):  # ID 可以是str，也可以是list
    crruent_time = lambda:int(round(time.time() * 1000))  #获取当前毫秒级时间戳
    t = '&t='+ str(crruent_time)
    callback = '&callback=json'
    isAll = '&isAll=true'
    isInner = '&isInner=true'
    baseURL = 'https://rate.tmall.com/listTagClouds.htm?itemId='

    if isinstance(ID,str):
        return baseURL+ID+isAll+isInner+t+callback
    
    elif isinstance(ID,list):
        urls = []
        for id in ID:
            urls.append(baseURL+id+isAll+isInner+t+callback)
        return urls #list
    