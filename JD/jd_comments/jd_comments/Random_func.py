#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/6/26 17:15
# @Author   : z_jian
# @contact  : zjian1425@gmail.com
# @File     : Random_func.py

import random
import pandas as pd

def get_referer(com_id):
    return str('https://item.jd.com/{0}.html'.format(com_id))

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

from jd_comments.settings import UA_list
def Random_Headers(com_id):

    headers = {
        'user-agent':random.choice(UA_list),
        'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'cache - control': 'max - age = 0',
        'accept - language': 'zh - CN, zh;q = 0.9',
        'accept_encoding':'gzip,deflate,br',
        'upgrade-insecure-requests':'1',
        'referer':get_referer(com_id)   #call get_referer
    }
    return headers

def Random_IpProxy():
    '''read ip_pool'''
    df = pd.read_csv('D:\JNBY_com_comments\proxiy_pool\ip_pool.csv')
    data = list(df['IP'])
    '''random return ip'''
    return {'https':random.choice(data)}


from jd_comments.settings import CookiesList

def Random_Cookies():
    return random.choice(CookiesList)
