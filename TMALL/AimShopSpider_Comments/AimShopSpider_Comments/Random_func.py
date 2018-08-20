#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/6/26 17:15
# @Author   : z_jian
# @contact  : zjian1425@gmail.com
# @File     : Random_func.py

import random
import pandas as pd

def get_referer(com_id):
    return str('https://detail.tmall.com/item.htm?id='+com_id)

def Random_WaitTime(flag):
    '''generate random waitting time'''
    if flag=='turnover':
        '''turnover page waitting'''
        t1 = random.uniform(5,10)
        print('now turnover page waitting time:{0}'.format(t1))
        return t1 #generate float

    elif flag=='jump':
        '''jump waitting'''
        t2 = random.uniform(5,10)
        print('now_jump_waitting:{0}'.format(t2))
        return t2 #generate float

    elif flag=='sleep':
        '''sleep waitting'''
        t3 = random.uniform(60,120)
        print('sleep waitiing:{0}'.format(t3))
        return t3 #generate float

    else:
        print('flag only input 0/1,now imput{0}'.format(flag))

from AimShopSpider_Comments.settings import UA_List

def Random_Headers(com_id):

    headers = {
        'user-agent':random.choice(UA_List),
        'accept':'*/*',
        'accept_encoding':'gzip,deflate,br',
        'if-none-match':'W/"jsDmDufd+vdwptc6XYWSjw=="',
        'referer':get_referer(com_id) #call get_referer
    }
    return headers

def Random_IpProxy():
    '''read ip_pool'''
    df = pd.read_csv('AimShopSpider_Comments\proxyip.csv')
    data = list(df['IP'])
    '''random return ip'''
    return {'https':random.choice(data)}
from AimShopSpider_Comments.settings import cookies
def Random_Cookies():
    '''cookies dict'''
    return cookies
