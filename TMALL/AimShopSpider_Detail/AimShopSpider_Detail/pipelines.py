# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
import logging
from AimShopSpider_Detail.settings import Database as db,account



# 实例化
logger = logging.getLogger('Error')
# 格式化输出Error信息
formatter = logging.Formatter('%(asctime)s %(levelname)-8s: %(message)s')
# 创建文件，指定编码方式
file_handler = logging.FileHandler('Error.log', encoding='utf-8')
# 格式设定
file_handler.setFormatter(formatter)
# 加载日志处理器
logger.addHandler(file_handler)
# 设定输出级别
# CRITICAL 50，ERROR 40，WARNNING 30,INFO 20,DEBUG 10,NOSET 0
# 优先级别：50 > 40 > 30 >20 > 10 > 0
logger.setLevel(logging.ERROR)


def log(info):
    logger.info(info)

import datetime
class AimshopspiderDetailPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(db['IP'],db['USERNAME'],db['PASSWORD'],db['DB_NAME'],charset='utf8')
        self.cursor = self.conn.cursor()


    def process_item(self, item, spider):
        c_time = datetime.datetime.now().strftime('%Y-%m-%d')  # 数据库表中com_id 和 crawls_time 设置了联合主键
        do_insert = ''' insert into commodity_detail(com_id,title,o_price,n_price,sale_nums,comment_nums,
        fav_nums,product_params,shop_name,crawls_time
                    )values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
        param = (item['com_id'],item['title'],item['o_price'],item['n_price'],item['sale_nums'],item['comment_nums'],
                 item['fav_nums'],item['product_params'],spider.name,c_time)
        try:
            self.cursor.execute(do_insert,param)
            self.conn.commit()
        except Exception as e:
            print('when insert occur error as followed:')
            with open('Error.log', 'a+') as f:
                f.write(e.args[1]+'\n')
            f.close()
