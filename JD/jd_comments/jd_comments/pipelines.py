# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from time import ctime
from jd_comments.settings import Database as DB


class JdCommentsPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(DB['IP'], DB['USERNAME'], DB['PASSWORD'], DB['DB_NAME'], charset='utf8')
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):

        do_insert = '''insert into jd_comments(com_url,tag_string,content,
                        creation_time,useful_vote_count,useless_vote_count,
                        score,product_color,product_size,user_level_name,
                        user_client_show,shop_name)values (
                %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
        params = (item['com_url'], item['tag_string'], item['content'], item['creation_time'],
                  item['useful_vote_count'],item['useless_vote_count'], item['score'],
                  item['product_color'], item['product_size'],item['user_level_name'],
                  item['user_client_show'], item['shop_name'])
        try:
            self.cursor.execute(do_insert, params)
            self.conn.commit()
            print('[%s] %s'%(ctime(),'insert successed!!!'))
        except Exception as e:
            with open('Error.log', 'a+') as f:
                f.write(e.args[0] + '\n')
            f.close()


        return item
