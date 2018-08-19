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

def Random_Headers(com_id):
    '''switch ua'''
    UA_List = [
        'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52',
        'Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)',
        'Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
        'Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)',
        'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)',
        'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)',
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)',
        'Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6',
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1',
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0',
        'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36',
        'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)',
        'Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+',
        'Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999',
        'MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
        'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
        'Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
        'Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
        'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;',
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)',
        'Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+',
        'Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13',
        'Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10',
        'NOKIA5700/ UCWEB7.0.2.37/28/999'
    ]
    '''return dict'''
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

def Random_Cookies():
    '''cookies dict'''
    cookies = {
        'cna': 'PmyXXXXPxxj3B/X',
        'hng': 'XXX',
        'uss': 'XXXX',
        'uc1': 'UoTfK7JXXX3D%3D',
        'cookie14': 'UoTfK7JXXX3D%3D',
        'lng': 'zh_CN',
        'cookie16': 'Vq8l%2BKCLXXXFWHXX8fwqXXXXD%3D',
        'existShop': 'false',
        'cookie21': 'VqXXXLivbS%2FaOXXX%3XX3D',
        'tag': '8',
        'cookie15': 'UXXX3xD8xYTXXX3D',
        'pas': '0',
        'uc3': 'BMcuoXXXXuZeg%3D',
        'nk2': 'BMcuo5TXXXeg%3D',
        'id2': 'UXXXxC0Q%2BLswXXXD',
        'vt3': 'F8dBzrXXXDLeA1R8%3D',
        'lg2': 'W5iHLLyFOGW7aA%3D%3D',
        'tracknick': 'g1200dragon',
        '_l_g_': 'Ug%3D%3D',
        'ck1': 'ASDS',
        'unb': '1832706723',
        'lgc': 'XXXXXX',
        'cookie1': 'BdH8XXXXXXXXzG2POmtOTP5QCZa60Q10roJtr7vfI%3D',
        'login': 'true',
        'cookie17': 'UonYs9xXXXXXXw%3D%3D',
        'cookie2': '1X2327XXXXX6fafaaXX3',
        '_nk_': 'XXXXXXXXXX',
        't': '0bfafXXXXXXXXXX4f2946010b37f',
        'csg': 'a61XXXXXX3',
        'skt': '47dXXXXXXc9',
        '_tb_token_': 'eXXXXXXX104',
        'cq': 'ccXXX0',
        'isg': 'BO7uPQyXXXXXXXaGMpA0DXXXfGs-45XXX8C-ZT5tyXXXoB'
    }
    return cookies
