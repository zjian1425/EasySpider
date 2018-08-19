#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File     : CleanDataAndStore.py
# @Author   : Zjian
# @Time     : 18-7-23
# @Desc     :In haiming
# @Contact  :zjian1425@gmail.com
#@Software  : PyCharm
import pymysql

class DataPiplelines(object):

    def __init__(self):
        """connect database"""
        self.conn = pymysql.connect('IP','NAME','PASSWD','DB_NAME',charset='utf8')
        self.cursor = self.conn.cursor()
    
    def StoreData(self,data,string):
        """存储工作"""
        for id in data:
            do_insert = """insert into {0}(com_id)values (%s)""".format(string+'_id')
            try:
                self.cursor.execute(do_insert,id)
                self.conn.commit()
            except Exception as e:
                print('当前插入时发生如下错误：')
                print(e)
            
    def DataFlow(self,data,string):
        self.StoreData(data,string)
        
    def __del__(self):
        """close connect"""
        self.cursor.close()
        self.conn.close()