#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : PipeLines.py
# @Author: zjian
# @Date  : 18-8-25
# @Contact  :zjian1425@gmail.com 
#@Software : PyCharm

__doc__ = '''数据存储模块'''

import pymysql
from models.Settings import  Databases as db

class Pipeline(object):

    def __init__(self,**kwargs):
        self.conn = pymysql.connect(db['ip'],db['username'],db['password'],db['db_name'],charset='utf8')
        self.cursor = self.conn.cursor()
        self.kwargs = kwargs

    def process_item(self, item, spider):

        do_insert = ''' insert into Hstyle(title,bd,goods_nums,o_price,n_price,sale_count,score,
        comment_nums,brand,c_size,color)values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''

        params = (
            self.kwargs['title'], self.kwargs['bd'], self.kwargs['goods_nums'], self.kwargs['o_price'], self.kwargs['n_price'], self.kwargs['sale_count'],
            self.kwargs['score'], self.kwargs['comment_nums'], self.kwargs['brand'], self.kwargs['c_size'], self.kwargs['color'])
        try:
            self.cursor.execute(do_insert,params)
            self.conn.commit()
        except Exception as e:
            with open ('run.log','a+') as f:
                f.write(e.args[1]+'\n')
            f.close()#由于with为上下文管理(此处可以不写)，我们可以做一些对象的开始操作和退出操作,还能对异常进行处理

    def __del__(self):
        print('当前connect即将断开...')
        self.cursor.close()
        self.conn.close()
