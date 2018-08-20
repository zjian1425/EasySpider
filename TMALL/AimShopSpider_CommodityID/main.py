#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File     : main.py
# @Author   : Zjian
# @Time     : 18-7-24
# @Desc     :In haiming
# @Contact  :zjian1425@gmail.com
#@Software  : PyCharm


import sys
import os
from scrapy.cmdline import execute

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(['scrapy','crawl','VeroModa'])

# 'HM','Hstyle','LeTin','Loytio','Only','PeaceBird','Qimi','Uniqlo','VeroModa','Zara'
