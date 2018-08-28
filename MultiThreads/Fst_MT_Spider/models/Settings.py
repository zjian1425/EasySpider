#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Settings.py
# @Author: zjian
# @Date  : 18-8-24
# @Contact  :zjian1425@gmail.com 
#@Software : PyCharm

__doc__='''配置文件'''

Databases = {
    'ip':'localhost',
    'username':'zjian',
    'password':'123456',
    'db_name':'db_ecommerce',
}



start_urls = [
                  'http://www.handu.com/category-225-b0-min0-max0-attr0-', #hstyle
                  'http://www.handu.com/category-10330-b0-min0-max0-attr0-',#nanaday
                  'http://www.handu.com/category-10314-b0-min0-max0-attr0-',#forqueens
                  'http://www.handu.com/category-328-b0-min0-max0-attr0-',#niBBuns
                  'http://www.handu.com/category-155-b0-min0-max0-attr0-',#souline
                  ]


def init_url():
    urls_list = []
    for t in start_urls:
        if t =='http://www.handu.com/category-225-b0-min0-max0-attr0-':
            for i in range(1,50):
                url = t+'{0}-sell_count-desc.html'.format(i)
                urls_list.append(url)

        elif t=='http://www.handu.com/category-10330-b0-min0-max0-attr0-':
            for i in range(1,9):
                url = t+'{0}-sell_count-desc.html'.format(i)
                urls_list.append(url)

        elif t=='http://www.handu.com/category-10314-b0-min0-max0-attr0-':
            for i in range(1,8):
                url = t+'{0}-sell_count-desc.html'.format(i)
                urls_list.append(url)

        elif t=='http://www.handu.com/category-328-b0-min0-max0-attr0-':
            for i in range(1,10):
                url = t+'{0}-sell_count-desc.html'.format(i)
                urls_list.append(url)

        elif t=='http://www.handu.com/category-155-b0-min0-max0-attr0-':
            for i in range(1,5):
                url = t+'{0}-sell_count-desc.html'.format(i)
                urls_list.append(url)
    return urls_list
