#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Crawler.py
# @Author: zjian
# @Date  : 18-9-3
# @Contact  :zjian1425@gmail.com 
#@Software : PyCharm

import requests
import threading
import time
import json
import datetime
import pymysql
from Setting import *
from queue import Queue


#数据取出 mysql ——> physicalQueue  单个线程
class PhysicalAddress(threading.Thread):

    def __init__(self, threadName, physicalQueue):
        super(PhysicalAddress, self).__init__()
        self.threadName = threadName
        self.physicalQueue = physicalQueue
        self.conn = pymysql.connect(DB_info['host'],DB_info['username'],DB_info['password'],
                                    DB_info['db_name'],charset='utf8')
        self.cursor = self.conn.cursor()

    def run(self):
        print('[INFO]启动%s' % self.threadName)
        self.execute()
        print('[INFO]%s线程结束' % self.threadName)
    def execute(self):
        do_select = do_select_sql #配置在Setting中
        self.cursor.execute(do_select)
        tuple = self.cursor.fetchall()
        for physical_addr in tuple:
            self.physicalQueue.put(physical_addr[0])

#请求处理 physicalQueue ——> dataQueue
class CrawlGIS(threading.Thread):

    def __init__(self, threadName, physicalQueue,dataQueue,BaseUrl):
        super(CrawlGIS, self).__init__()
        self.threadName = threadName
        self.dataQueue = dataQueue
        self.BaseUrl = BaseUrl
        self.physicalQueue = physicalQueue
        # self.physical_Address = physical_Address
    def run(self):
        print('[INFO]启动%s' % self.threadName)
        while not EXIT_FLAG:
            try:
                physical_Address = self.physicalQueue.get(False)
                url = self.BaseUrl + physical_Address
                self.extract_json(url,physical_Address)
            except Exception as e:
                pass
        print('[INFO]%s线程结束' % self.threadName)
    def Requests(self,url,physical_Address):
        cnt = 0  #控制循环次数
        flag = False  #判断请求成功与否，默认为失败
        dict_type = {}
        while cnt<3: #失败请求尝试3次
            response = requests.get(url=url)

            if response.status_code==200:
                flag = True
                response.content.decode('utf8')
                dict_type = json.loads(response.content.decode('utf8'))
                break #退出请求循环

            else:
                if cnt==2:
                    print('当前请求地址：%s 请求失败'%physical_Address)
                    now_time = str(datetime.datetime.now().strftime('%Y-%m-%d'))
                    with open('run.log','a+') as f:
                        f.write(physical_Address+'请求失败\n'+now_time)
                    break #退出请求循环
                else:
                    cnt +=1

        if flag:
            return dict_type  # 返回经过json.loads处理的dict格式对象
        else:
            return None #失败返回为空
    def extract_json(self,url,physical_Address):
        '''
        处理请求后返回的字典格式的数据，从中提取出与物理地址相对应的经纬度信息
        :return: 封装好的item给 put进itemQueue 队列 利用self.store_data()方法执行入库操作
        '''
        response = self.Requests(url,physical_Address)
        if response: #返回不为空
            physical_address = physical_Address
            geo_location = response['geocodes'][0]['location']
            geo_list = geo_location.split(',')
            longitude = geo_list[0]
            latitude = geo_list[1]
            city_code = response['geocodes'][0]['citycode']
            item = (physical_address, longitude, latitude, city_code)
            self.dataQueue.put(item) #放入数据队列

#数据入库 dataQueue ——> mysql
class Store_data(threading.Thread):
    def __init__(self, threadName, dataQueue,lock):
        super(Store_data, self).__init__()
        self.threadName = threadName
        self.dataQueue = dataQueue
        self.conn = pymysql.connect(DB_info['host'],DB_info['username'],DB_info['password'],
                                    DB_info['db_name'],charset='utf8')
        self.cursor=self.conn.cursor()
        self.lock = lock
    def run(self):
        print('[INFO]启动%s' % self.threadName)
        while not SEXIT_FLAG:
            try:
                item = self.dataQueue.get(False)
                self.execute(item)
            except:
                pass
        print('[INFO]%s线程结束' % self.threadName)

    def execute(self,item):
        do_insert = '''insert into GEO(physical_address,longitude,latitude,city_code)values (%s,%s,%s,%s)'''
        with self.lock:
            try:
                self.cursor.execute(do_insert,item)
                self.conn.commit()
            except Exception as e:
                print('[INFO]再插入数据时发生如下故障:')
                print(e)

    def __del__(self):
        with self.lock:
            self.cursor.close()
            self.conn.close()

EXIT_FLAG = False
SEXIT_FLAG = False

def main():
    physicalQueue = Queue()
    dataQueue = Queue()

    Fetchall = PhysicalAddress('Fetch data thread', physicalQueue)
    Fetchall.start() #启动取数据线程（single）
    Fetchall.join()

    threads_crawl = []
    for i in range(190):
        threadName = 'threads_crawl' + str(i)
        thread_C = CrawlGIS(threadName, physicalQueue, dataQueue, BaseUrl)
        threads_crawl.append(thread_C)
    for thread_C in threads_crawl:
        thread_C.start()
    lock = threading.Lock()
    threads_store = []
    for i in range(100):
        threadName = 'threads_store' + str(i)
        thread_S = Store_data(threadName,dataQueue,lock)
        threads_store.append(thread_S)
    for thread_S in threads_store:
        thread_S.start()

    while not physicalQueue.empty():
        pass
    global EXIT_FLAG
    EXIT_FLAG = True
    for i in threads_crawl:
        i.join()

    while not dataQueue.empty():
        pass
    global SEXIT_FLAG
    SEXIT_FLAG = True
    for i in threads_store:
        i.join()

if __name__=='__main__':
    start = time.time()
    main()
    print('[INFO_Time] 总耗时 %s'%(time.time() - start))