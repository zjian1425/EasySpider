#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Spider2.py
# @Author: zjian
# @Date  : 18-8-27
# @Contact  :zjian1425@gmail.com 
#@Software : PyCharm

from queue import Queue
import threading
from lxml import etree
import requests
import time
import pymysql

class ThreadCrawl(threading.Thread):
    def __init__(self,threadName,dataQueue,urlQueue):
        super(ThreadCrawl, self).__init__()
        #线程名
        self.threadName = threadName
        #数据队列
        self.dataQueue = dataQueue
        #url队列
        self.urlQueue = urlQueue
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'}
    def run(self):
        print('[INFO]启动%s'%self.threadName)
        while not C_EXIT_FLAG:
            try:
                url = str(self.urlQueue.get(False))
                content = requests.get(url=url,headers=self.headers).text
                time.sleep(1)
                self.dataQueue.put(content)
            except:
                pass
        print('[INFO]%s线程结束'%self.threadName)

class ThreadParse(threading.Thread):

    def __init__(self, threadName, dataQueue,resQueue):
        super(ThreadParse, self).__init__()
        self.threadName = threadName
        self.dataQueue = dataQueue
        self.resQueue = resQueue
    def run(self):
        print('[INFO] 启动 %s 线程'%self.threadName)
        while not P_EXIT_FLAG:
            try:
                response = self.dataQueue.get(False)
                self.parse(response)
            except:
                pass
        print('[INFO] %s 线程结束'%self.threadName)

    def parse(self,response):
        # 解析为HTML DOM
        response = etree.HTML(response)
        title = ''.join(response.xpath('//*[@id="goods_detail_1"]/h1/text()')).strip()
        try:
            bd = response.xpath('//*[@id="goods_detail_1"]/h1/em/a/span/text()')[0]
        except:
            bd = ''
        goods_nums = response.xpath('//*[@id="goods_detail_1"]/ul/li[1]/span[1]/text()')[0]  # 商品货号
        o_price = response.xpath('//*[@id="goods_detail_1"]/ul/li[1]/del/text()')[0]
        n_price = response.xpath('//*[@id="goods_detail_1"]/ul/li[2]/em/text()')[0]
        sale_count = response.xpath('//*[@id="goods_detail_1"]/ul/li[3]/span/text()')[0]
        comment_nums = response.xpath('//*[@id="goods_detail_1"]/ul/li[4]/span[2]/a/text()')[0]
        score = response.xpath('//*[@id="goods_detail_1"]/ul/li[4]/span[1]/em/@title')[0]
        brand = response.xpath('//*[@id="J_attrBrandName"]/text()')[0]
        c_size = response.xpath('//*[@id="J_AttrUL"]/li[3]/text()')[0].replace('\n', '').replace(' ', '').replace(
            '\xa0', ',')
        color = response.xpath('//*[@id="J_AttrUL"]/li[4]/text()')[0].replace('\n', '').replace(' ', '').replace('\xa0',
                                                                                                                 ',')

        item = {'title': title,
                'bd': bd,
                'goods_nums': goods_nums,
                'o_price': o_price,
                'n_price': n_price,
                'sale_count': sale_count,
                'comment_nums': comment_nums,
                'score': score,
                'brand': brand,
                'c_size': c_size,
                'color': color
                }
        self.resQueue.put(item)

class ThreadStore(threading.Thread):
    def __init__(self, threadName, resQueue,lock):
        super(ThreadStore, self).__init__()
        self.threadName = threadName
        self.resQueue = resQueue
        self.lock = lock
        self.conn = pymysql.connect('localhost','zjian','123456','db_ecommerce',charset='utf8')
        self.cursor = self.conn.cursor()
        self.conn.ping(True)
    def run(self,):
        print('[INFO] 启动%s线程进行存储' % self.threadName)
        while not S_EXIT_FLAG:
            try:
                item = self.resQueue.get(False)
                self.store(item)
            except:
                pass
        print('[INFO] 结束%s存储线程' % self.threadName)
    def store(self,item):
       insert_sql = '''insert into Hstyle(title,bd,goods_nums,o_price,n_price,sale_count,score,comment_nums,brand,c_size,color)
       values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
       params = (item['title'],item['bd'],item['goods_nums'],item['o_price'],item['n_price'],item['sale_count'],
                 item['score'],item['comment_nums'],item['brand'],item['c_size'],item['color'])
       with self.lock:
            try:
               self.cursor.execute(insert_sql,params)
               self.conn.commit()
            except Exception as e:
               print(e)

    def __del__(self):
        with self.lock:
            self.cursor.close()
            self.conn.close()

C_EXIT_FLAG = False
P_EXIT_FLAG = False
S_EXIT_FLAG = False

def main():
    #url队列
    urlQueue = Queue()
    url_list = ['http://www.handu.com/goods-1073166.html',
                'http://www.handu.com/goods-1072736.html',
                'http://www.handu.com/goods-1072705.html',
                'http://www.handu.com/goods-1072183.html',
                'http://www.handu.com/goods-1072173.html',
                'http://www.handu.com/goods-1070243.html',
                'http://www.handu.com/goods-1069943.html',
                'http://www.handu.com/goods-1068374.html',
                'http://www.handu.com/goods-1068374.html',
                'http://www.handu.com/goods-1068342.html',
                'http://www.handu.com/goods-1066902.html',
                'http://www.handu.com/goods-1065701.html',
                'http://www.handu.com/goods-1065372.html',
                'http://www.handu.com/goods-1064926.html',
                'http://www.handu.com/goods-1074042.html',
                'http://www.handu.com/goods-1074019.html',
                'http://www.handu.com/goods-1074003.html',
                'http://www.handu.com/goods-1074004.html',
                'http://www.handu.com/goods-1074001.html',
                'http://www.handu.com/goods-1073990.html',
                'http://www.handu.com/goods-1073904.html',
                'http://www.handu.com/goods-1073867.html',
                'http://www.handu.com/goods-1073866.html',
                'http://www.handu.com/goods-1073854.html',
                'http://www.handu.com/goods-1073853.html',
                'http://www.handu.com/goods-1073846.html',
                'http://www.handu.com/goods-1073846.html',
                'http://www.handu.com/goods-1073845.html',
                'http://www.handu.com/goods-1073831.html',
                'http://www.handu.com/goods-1073825.html',
                'http://www.handu.com/goods-1073823.html',
                'http://www.handu.com/goods-1073822.html',
                'http://www.handu.com/goods-1073814.html',
                'http://www.handu.com/goods-1073813.html',
                'http://www.handu.com/goods-1073812.html',
                'http://www.handu.com/goods-1073807.html',
                'http://www.handu.com/goods-1073804.html',
                'http://www.handu.com/goods-1073783.html',
                'http://www.handu.com/goods-1073756.html',
                'http://www.handu.com/goods-1073746.html',
                'http://www.handu.com/goods-1073751.html',
                'http://www.handu.com/goods-1073744.html',
                'http://www.handu.com/goods-1073737.html',
                'http://www.handu.com/goods-1073714.html',
                'http://www.handu.com/goods-1073672.html',
                'http://www.handu.com/goods-1073638.html']
    #将url添加进Queue
    for url in url_list:
        urlQueue.put(url)

    #请求response队列
    dataQueue = Queue()

    #结果队列
    resQueue = Queue()
    #创建锁
    lock = threading.Lock()

    #创建线程名列表
    # crawllist =['Crawl-thds-1','Crawl-thds-2','Crawl-thds-3','Crawl-thds-4','Crawl-thds-5','Crawl-thds-6','Crawl-thds-7','Crawl-thds-8','Crawl-thds-9','Crawl-thds-10']
    #抓取线程列表
    threads_crawl = []
    for i in range(len(url_list)):   #经过测试发现在一定范围内线程数越多执行速度越快，其他影响因素：网速
        threadName = 'Crawl-thds-'+str(i)
        thread_C = ThreadCrawl(threadName,dataQueue,urlQueue)
        threads_crawl.append(thread_C)

    #开启线程
    for thread_C in threads_crawl:
        thread_C.start()

    #创建解析线程名
    # parselist = ['Parse-thds-1','Parse-thds-2','Parse-thds-3','Parse-thds-4','Parse-thds-5']
    #解析线程列表
    threads_parse = []
    # for threadName in parselist:
    for i in range(len(url_list)):
        threadName = 'Parse-thds-'+str(i)
        thread_P = ThreadParse(threadName,dataQueue,resQueue)
        threads_parse.append(thread_P)

    for thread_P in threads_parse:
        thread_P.start()

    #存储线程列表
    threads_Store = []
    for i in range(len(url_list)):
        threadName = 'Store-thds-' + str(i)
        thread_S = ThreadStore(threadName,resQueue,lock)
        threads_Store.append(thread_S)

    for thread_S in threads_Store:
        thread_S.start()

    #等待url请求队列中为空，采集线程退出循环
    while not urlQueue.empty():
        pass
    global C_EXIT_FLAG
    C_EXIT_FLAG = True

    for thread_C in threads_crawl:
        thread_C.join()

    while not dataQueue.empty():
        pass
    global P_EXIT_FLAG
    P_EXIT_FLAG = True

    for thread_P in threads_parse:
        thread_P.join()
    # while not resQueue.empty(): #打印看看
    #     print(resQueue.get())
    while not resQueue.empty():
        pass

    global S_EXIT_FLAG
    S_EXIT_FLAG = True

    for thread_S in threads_Store:
        thread_S.join()

if __name__=='__main__':
    start = time.time()
    main()
    print('[INFO]耗时%s'%(time.time()-start))