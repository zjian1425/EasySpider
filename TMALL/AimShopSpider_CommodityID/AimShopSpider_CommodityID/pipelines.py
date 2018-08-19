# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class AimshopspiderCommodityidPipeline(object):
    def __init__(self):
        """connect database"""
        self.conn = pymysql.connect('IP','NAME','PASSWD','DB_NAME',charset='utf8')
        self.cursor = self.conn.cursor()
        
        
    def process_item(self, item, spider):

        do_insert = """insert into commodity_id(com_id,shop_name)values(%s,%s)"""

        #因为接收的是一个list，所以需要遍历出list中的com_id
        for i in item['com_id_list']:
            params = (i,item['shop_name'])
            try:
                self.cursor.execute(do_insert,params)
                self.conn.commit()
            except Exception as e:
                print("when insert the com_id occured error as follows:")
                print(e)
