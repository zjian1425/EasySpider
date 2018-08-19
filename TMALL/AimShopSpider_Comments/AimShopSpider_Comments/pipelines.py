# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class AimshopspiderCommentsPipeline(object):
    AllCommentsName = ['HM', 'Hstyle', 'LeTin', 'Loytio', 'Only',
                       'PeaceBird', 'Qimi', 'Uniqlo', 'Veromoda',
                       'Zara']
    def __init__(self):
        self.conn = pymysql.connect('XXXX','XXX','XXXX','XXXXXXX',charset='utf8')
        self.cursor = self.conn.cursor()
        
    def process_item(self, item, spider):
        #全部评论专用pipeline对象
        if spider.name in self.AllCommentsName:
            '''data store_function'''
            do_insert = '''insert into comments(auctionSku,rateContent,reply,rateDate,
            tradeEndTime,com_id,crawls_time)VALUES (%s,%s,%s,%s,%s,%s,%s)'''
            prams = (item['auctionSku'], item['rateContent'], item['reply'], item['rateDate'],
                     item['tradeEndTime'], item['com_id'], item['crawls_time'])
            self.cursor.execute(do_insert, prams)
            self.conn.commit()  # save
            print('now_com_id:{0}comments store successfully!'.format(item['com_id']))
       
        #标签词专用pipeline对象
        else:
            do_insert = '''insert into tag_words(com_id,tag,posi,tag_count,
            crawls_time,id,weight)VALUES (%s,%s,%s,%s,%s,%s,%s)'''
            prams = (item['com_id'], item['tag'], item['posi'], item['tag_count'],
                     item['crawls_time'],item['c_id'],item['weight'])
            self.cursor.execute(do_insert, prams)
            self.conn.commit()  # save
            print('now_com_id:{0}comments store successfully!'.format(item['com_id']))


