#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : main.py
# @Author: zjian
# @Date  : 18-8-23
# @Contact  :zjian1425@gmail.com 
#@Software : PyCharm

import sys
import os
from scrapy.cmdline import execute

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(['scrapy','crawl','VM'])