# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import pymysql

class JdCommoditydetailPipeline(object):

    def __int__(self):
        self.conn = pymysql.connect('183.129.168.211','hexi','hexi123','db_ecommerce',charset='utf8')
        self.cursor = self.conn.cursor()

    def process_item(self,item,spider):

        do_insert = '''insert into jd_commoditydetail(com_url,title,n_price,o_price,comment_nums,
        product_params,shop_name,fav_rate,tag,good,mid,bad,po_tu)values (
        %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
        params = (item['com_url'],item['title'],item['n_price'],item['o_price'],item['comment_nums'],
                  item['product_params'],item['shop_name'],item['fav_rate'],item['tag'],item['good'],
                  item['mid'],item['bad'],item['po_tu'])
        try:
            self.cursor.execute(do_insert,params)
            self.conn.commit()
        except Exception as e:
            with open('Error.log','a+') as f:
                f.write(e.args[1]+'\n')
            f.close()



        return item
