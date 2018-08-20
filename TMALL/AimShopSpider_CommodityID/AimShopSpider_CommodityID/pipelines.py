# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
import datetime
from AimShopSpider_CommodityID.settings import Database as db


class AimshopspiderCommodityidPipeline(object):
    def __init__(self):
        """connect database"""
        self.conn = pymysql.connect(db['IP'],db['USERNAME'],db['PASSWORD'],db['DB_NAME'],charset='utf8')
        self.cursor = self.conn.cursor()
        
        
    def process_item(self, item, spider):
        c_time = datetime.datetime.now().strftime('%Y-%m-%d')   #数据库表中com_id 和 crawls_time 设置了联合主键
        do_insert = """insert into tm_commodityid(com_id,shop_name,crawls_time)values(%s,%s,%s)"""

        #因为接收的是一个list，所以需要遍历出list中的com_id
        for i in item['com_id_list']:
            params = (i,item['shop_name'],c_time)
            try:
                self.cursor.execute(do_insert,params)
                self.conn.commit()
            except Exception as e:
                print("when insert the com_id occured error as follows:")
                print(e)
