#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File     : test.py
# @Author   : Zjian
# @Time     : 18-7-25
# @Desc     :In haiming
# @Contact  :zjian1425@gmail.com
#@Software  : PyCharm

# import re
#
# a = """https://rate.tmall.com/list_detail_rate.htm?itemId=552915091614&sellerId=420567757&currentPage=9"""
#
# re.match('.*currentPage=(\d.*)',a).group(1)
# # print(a)
# exp = lambda :re.match('(.*currentPage=)\d.*',a).group(1)
#
# print(type(exp()))
# # s = lambda x:x+1
# # print(s(1))


# ips={'http':'12.12.12',
#      'http':'13.13.13.13',
#      'http':'14.14.14.14'}
#
# '''overwrite Download middlewares'''
# class NewDownloaderMiddleware(object):
#     http_n = 0
#     def process_request(self, request, spider):
#         n = NewDownloaderMiddleware.http_n
#         n = n if n< len(ips['http']) else 0
#         request.meta['proxy'] =
#         pass