#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/8/3 14:28
# @Author   : z_jian
# @contact  : zjian1425@gmail.com
# @File     : test.py

import re


a = 'https://sclub.jd.com/comment/p' \
    'roductPageComments.action?&score=0&sortType=5' \
    '&page=0&pageSize=10&productId=26189257084'



s = str(int(re.match('.*?page=(\d+).*?',a).group(1)) +1)
b = re.match('(.*?page=)\d+(.*?)',a).group(1)
c = re.match('(.*?page=)\d+(.*)',a).group(2)
print(s)
print(b)
print(c)
print(b+s+c)