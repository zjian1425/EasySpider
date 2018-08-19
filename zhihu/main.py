#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/4/4 16:02
# @Author   : z_jian
# @contact  : zjian1425@gmail.com
# @File     : main.py
from scrapy.cmdline import execute
import  sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
#启动爬虫的命令 scrapy crawl zhihu_following
execute(["scrapy","crawl","Zhihu"])
