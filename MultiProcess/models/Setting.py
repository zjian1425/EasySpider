#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Setting.py
# @Author: zjian
# @Date  : 18-8-30
# @Contact  :zjian1425@gmail.com 
#@Software : PyCharm

DB = {
    'host':'xxx',
    'username':'xxx',
    'password':'xxx',
    'db_name':'xxx',
}

only_num = [16,17,18,19,20,21]
veromoda_num = [4,7,12,17,22,23]

O_start_url= 'https://www.only.cn/goodsList.html?classifyIds=111163'
V_start_url= 'https://www.veromoda.com.cn/goodsList.html?classifyIds=111835'

#控制浏览器不显示图片
Prefs = {
    'profile.default_content_setting_values':{
        'images':2
    }
}