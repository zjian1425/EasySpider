#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test.py
# @Author: zjian
# @Date  : 18-7-29
# @Contact  :zjian1425@gmail.com 
#@Software : PyCharm
#
#
# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.implicitly_wait(15)
# driver.get('')
# a = driver.page_source
# print(driver.page_source)

#
# try:
#     f =open('hah.txt','r')
# except Exception as e:
#     print('when insert occur error as followed:')
#     with open('Erro1r.log', 'a+') as f:
#         f.write(e.args[1]+'\n')
# pass
import requests

# a = '访问太快了,请休息一下吧'
# print(a)

a = requests.get()