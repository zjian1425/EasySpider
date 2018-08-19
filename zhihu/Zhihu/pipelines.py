# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# import MySQLdb
# import MySQLdb.cursors
# from twisted.enterprise import adbapi
import pymysql

class ZhihuPipeline(object):
    def process_item(self, item, spider):
        return item

class MysqlPipeline(object):
    #采用同步的方式插入数据库
    def __init__(self):
        self.conn = pymysql.connect('localhost','username','password','db_name',charset='utf8')
        self.cursor = self.conn.cursor()
    def process_item(self, item, spider):
        do_insert = """
insert into users_info_test (u_name,follwingCount,followerCount,gender,
edu,job,place,url_token,asks,answerCount,introduce)VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
"""
        param = (item["u_name"], item["follwingCount"], item["followerCount"], item["gender"], item["edu"],
                 item["job"], item["place"], item["url_token"], item["asks"], item["answerCount"], item["introduce"])
        # 由于爬取的数据存在重复，再插入的时候会存在primary key的冲突
        #primary key冲突异常处理
        try:
            self.cursor.execute(do_insert,param)
            self.conn.commit()
        #抛出异常
        except:
            print("已存在该数据")

