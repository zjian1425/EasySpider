# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class JdUrlPipeline(object):
    def __init__(self):
        """connect database"""
        self.conn = pymysql.connect('183.129.168.211', 'hexi', 'hexi123', 'db_ecommerce', charset='utf8')
        self.cursor = self.conn.cursor()
    def process_item(self, item, spider):
        do_insert = """insert into jd_url(com_url,shop_name)values(%s,%s)"""
        for i in item['com_url_list']:
            params =  (i,item['shop_name'])
            try:
                self.cursor.execute(do_insert,params)
                self.conn.commit()
            except Exception as e:
                with open('Error.log','a+') as f:
                    f.write(e.args[1]+'\n')
                f.close()



        return item
