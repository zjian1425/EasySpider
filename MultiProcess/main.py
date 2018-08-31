#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : main.py
# @Author: zjian
# @Date  : 18-8-30
# @Contact  :zjian1425@gmail.com 
#@Software : PyCharm


from Spider.Only import Omain
from Spider.Veromoda import Vmain
from multiprocessing import Process,Queue
from lxml import etree
from selenium import webdriver
from models.Setting import *
import time
import pymysql
import datetime
import os

class UrlCrawl(Process):
    def __init__(self, func, dataQueue):
        super(UrlCrawl, self).__init__()
        self.func = func
        self.dataQueue = dataQueue
    def run(self):
        self.func(self.dataQueue)

class CommodityCrawl(Process):

    def __init__(self, urlQueue, dataQueue, Pname):
        super(CommodityCrawl, self).__init__()
        self.urlQueue = urlQueue
        self.dataQueue = dataQueue
        self.name = Pname
        opt = webdriver.ChromeOptions()
        opt.add_experimental_option('prefs', Prefs)  # 从Setting中引用
        self.driver = webdriver.Chrome(chrome_options=opt)
        self.driver.implicitly_wait(10)  # 隐式等待10S

    def run(self):
        self.parse()

    def requests(self,url):
        self.driver.execute_script('window.scrollBy(0,3000)')
        self.driver.execute_script('window.scrollBy(0,4000)')
        self.driver.execute_script('window.scrollBy(0,3000)')
        content = self.driver.page_source.encode('utf8','ignore')
        return content

    def parse(self):
        '''
        解析商品详细字段
        :return:
        '''
        while not UEXIT_FLAG:
            list = self.urlQueue.get(False)
            url = list[0]
            brand = list[1]
            try:
                response = self.requests(url)
                response = etree.HTML(response)

                title = response.xpath('')
                goods_num = response.xpath('')
                n_price = response.xpath('')
                o_price = response.xpath('')
                color = response.xpath('')
                materials = response.xpath('')
                c_time = datetime.datetime.now().strftime('%Y-%m-%d')
                item = {
                    'title':title,
                    'goods_num':goods_num,
                    'n_price':n_price,
                    'o_price':o_price,
                    'color':color,
                    'materials':materials,
                    'url':url,
                    'c_time':c_time,
                    'brand':brand
                }

                self.dataQueue(item)
            except Exception as e:
                print('[INFO]抓取 %s时发生如下错误：'%url)
                print(e)

    def __del__(self):
        self.driver.quit()

class Store(Process):

    def __init__(self, dataQueue,Pname):
        super(Store, self).__init__()
        self.dataQueue = dataQueue
        self.Pname = Pname
        self.conn = pymysql.connect(DB['host'],DB['username'],DB['password'],DB['db_name'],charset='utf8')
        self.cursor = self.conn.cursor()

    def run(self):
        print('[INFO] 启动%s进程进行存储' % self.Pname)
        while not SEXIT_FLAG:
            try:
                item = self.dataQueue.get(False)
                self.store(item)
            except:
                pass
        print('[INFO] 结束%s存储进程' % self.Pname)

    def store(self,item):
        do_insert = '''insert into only_veromoda(url,title,goods_num,n_price,o_price,color,materials,brand
        ,c_time)values (%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
        params = (item['url'],item['title'],item['goods_num'],item['n_price'],item['o_price'],item['color'],
                  item['materials'],item['brand'],item['params'])
        try:
            self.cursor.execute(do_insert,params)
            self.conn.commit()
        except Exception as e:
            print(e)

    def __del__(self):
        self.cursor.close()
        self.conn.close()


func = [Omain,Vmain]
nloops = len(func)
UEXIT_FLAG = False
SEXIT_FLAG = False
def mainFunc():

    URLQueue = Queue()
    DataQueue = Queue()
    URLProcess_list = []
    for i in range(nloops):
        PU = UrlCrawl(func[i],URLQueue)
        URLProcess_list.append(PU)

    for P in URLProcess_list:
        P.start()

    DataProcess_list = []
    for i in range(5):
        Pname = '进程%s'.format(i)
        PD = CommodityCrawl(URLQueue,DataQueue,Pname)
        DataProcess_list.append(PD)

    for PD in DataProcess_list:
        PD.start()

    SProcess_list = []
    for i in range(10):
        Pname = '进程%s'.format(i)
        PS = Store(DataQueue,Pname)
        SProcess_list.append(PS)

    for PS in SProcess_list:
        PS.start()

    while not URLQueue.empty():
        pass
    global UEXIT_FLAG
    UEXIT_FLAG = True

    while not DataQueue.empty():
        pass
    global SEXIT_FLAG
    SEXIT_FLAG = True

    for P in URLProcess_list:
        P.join()

    for P in DataProcess_list:
        P.join()


if __name__ =='__main__':
    start = time.time()
    mainFunc()
    print('[INFO] 耗时 %s' % (time.time() - start))