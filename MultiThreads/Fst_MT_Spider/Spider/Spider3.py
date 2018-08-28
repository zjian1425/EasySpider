#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Spider3.py
# @Author: zjian
# @Date  : 18-8-27
# @Contact  :zjian1425@gmail.com 
#@Software : PyCharm
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Spider2.py
# @Author: zjian
# @Date  : 18-8-27
# @Contact  :zjian1425@gmail.com
# @Software : PyCharm

from queue import Queue
import threading
from lxml import etree
import requests
import time
import pymysql
from Fst_MT_Spider.models.Settings import init_url

class ThreadCrawlCom_URL(threading.Thread):

    def __init__(self, threadName, PageurlQueue, ComUrlQueue):
        super(ThreadCrawlCom_URL, self).__init__()
        self.threadName = threadName
        self.PageurlQueue = PageurlQueue
        self.ComUrlQueue = ComUrlQueue
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'}

    def run(self):
        print('[INFO]启动%s' % self.threadName)
        while not PC_EXIT_FLAG:
            try:
                url = str(self.PageurlQueue.get(False))
                content = requests.get(url=url, headers=self.headers).text
                time.sleep(1)
                self.ComUrlQueue.put(content) #将请求回的列表页内容放置于此
            except:
                pass
            print('[INFO]%s线程结束' % self.threadName)

class ThreadCrawl(threading.Thread):
    def __init__(self, threadName, dataQueue, urlQueue):
        super(ThreadCrawl, self).__init__()
        # 线程名
        self.threadName = threadName
        # 数据队列
        self.dataQueue = dataQueue
        # url队列
        self.urlQueue = urlQueue
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'}

    def run(self):
        print('[INFO]启动%s' % self.threadName)
        while not C_EXIT_FLAG:
            try:
                url = str(self.urlQueue.get(False))
                content = requests.get(url=url, headers=self.headers).text
                time.sleep(1)
                self.dataQueue.put(content)
            except:
                pass
        print('[INFO]%s线程结束' % self.threadName)

# 用以解析商品详情页
class ThreadParse(threading.Thread):

    def __init__(self, threadName, dataQueue, resQueue):
        super(ThreadParse, self).__init__()
        self.threadName = threadName
        self.dataQueue = dataQueue
        self.resQueue = resQueue

    def run(self):
        print('[INFO] 启动 %s 线程' % self.threadName)
        while not P_EXIT_FLAG:
            try:
                response = self.dataQueue.get(False)
                self.parse(response)
            except:
                pass
        print('[INFO] %s 线程结束' % self.threadName)

    def parse(self, response):
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
        c_size = response.xpath('//*[@id="J_AttrUL"]/li[3]/text()')[0].replace('\n', '').replace(' ', '').replace('\xa0', ',')
        color = response.xpath('//*[@id="J_AttrUL"]/li[4]/text()')[0].replace('\n', '').replace(' ', '').replace('\xa0',',')

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

#现在需要一个解析商品url的类，
class ThreadParseComUrl(threading.Thread):

    def __init__(self,threadName,urlQueue,ComUrlQueue):
        super(ThreadParseComUrl, self).__init__()
        self.threadName = threadName
        self.urlQueue = urlQueue
        self.ComUrlQueue = ComUrlQueue
    def run(self):
        print('[INFO] 启动 %s 线程' % self.threadName)
        while not PP_EXIT_FLAG:
            try:
                response = self.ComUrlQueue.get(False)
                self.parse(response)
            except:
                pass
        print('[INFO] %s 线程结束' % self.threadName)
    def parse(self,response):
        response = etree.HTML(response)
        """这里写提取逻辑"""
        for i in range(1,41):
            try:
                url = 'http://www.handu.com/'+response.xpath('//*[@id="cate_right"]/div[3]/div[1]/div[{0}]/div/div[1]/a/@href'.format(i))[0]
                self.urlQueue.put(url) #将url放入队列
            except:
                print('[info]当前%s节点不存在商品url'%i)
                continue

class ThreadStore(threading.Thread):
    def __init__(self, threadName, resQueue, lock):
        super(ThreadStore, self).__init__()
        self.threadName = threadName
        self.resQueue = resQueue
        self.lock = lock
        self.conn = pymysql.connect('localhost', 'zjian', '123456', 'db_ecommerce', charset='utf8')
        self.cursor = self.conn.cursor()
        self.conn.ping(True)

    def run(self, ):
        print('[INFO] 启动%s线程进行存储' % self.threadName)
        while not S_EXIT_FLAG:
            try:
                item = self.resQueue.get(False)
                self.store(item)
            except:
                pass
        print('[INFO] 结束%s存储线程' % self.threadName)

    def store(self, item):
        insert_sql = '''insert into Hstyle(title,bd,goods_nums,o_price,n_price,sale_count,score,comment_nums,brand,c_size,color)
       values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
        params = (item['title'], item['bd'], item['goods_nums'], item['o_price'], item['n_price'], item['sale_count'],
                  item['score'], item['comment_nums'], item['brand'], item['c_size'], item['color'])
        with self.lock:
            try:
                self.cursor.execute(insert_sql, params)
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
PC_EXIT_FLAG = False
PP_EXIT_FLAG = False

def main():

    pageQueue = Queue()# pageurl队列  （商品展示陈列页面，首页url）
    ComUrlQueue = Queue()  # 放置请求后返回的商品url队列（未解析）
    urlQueue = Queue()  # 将抓取到的商品url放置在此队列中（已解析）
    dataQueue = Queue()  # 放置请求后返回的(未经过parse解析的)商品数据队列
    resQueue = Queue()  # 结果队列 （已解析）
    lock = threading.Lock()# 创建锁

    pageurl_list = init_url()  #这里生成起始页面url列表
    for pageurl in pageurl_list:
        pageQueue.put(pageurl)

    #1.抓取商品url线程列表
    threads_crawlC = []
    for i in range(len(pageurl_list)):
        threadName = 'Crawl_URL-thds-' + str(i)
        thread_CC = ThreadCrawlCom_URL(threadName,pageQueue,ComUrlQueue)
        threads_crawlC.append(thread_CC)
    #1.1开启抓取商品url的线程
    for thread_CC in threads_crawlC:
        thread_CC.start()

    #2解析商品url线程列表
    threads_parseC = []
    for i in range(100):
        threadName = 'Parse_CC-thds-' + str(i)
        thread_PC = ThreadParseComUrl(threadName,urlQueue,ComUrlQueue)
        threads_parseC.append(thread_PC)
    #2.1开始解析商品url线程
    for thread_PC in threads_parseC:
        thread_PC.start()

    #3抓取商品详情线程列表
    threads_crawl = []
    for i in range(100):  # 经过测试发现在一定范围内线程数越多执行速度越快，其他影响因素：网速
        '''由于这里不知道url的长度，随着前一个的爬取，urlQueue的长度也是在不断增加的，所以这里先固定设置为100'''
        threadName = 'Crawl-thds-' + str(i)
        thread_C = ThreadCrawl(threadName, dataQueue, urlQueue)
        threads_crawl.append(thread_C)
    #3.1开启线程
    for thread_C in threads_crawl:
        thread_C.start()

    #4解析商品详情线程列表
    threads_parse = []
    # for threadName in parselist:
    for i in range(100):
        threadName = 'Parse-thds-' + str(i)
        thread_P = ThreadParse(threadName, dataQueue, resQueue)
        threads_parse.append(thread_P)
    #4.1 开启线程
    for thread_P in threads_parse:
        thread_P.start()

    #5存储线程列表
    threads_Store = []
    for i in range(100):
        threadName = 'Store-thds-' + str(i)
        thread_S = ThreadStore(threadName, resQueue, lock)
        threads_Store.append(thread_S)
    #5.1开启线程
    for thread_S in threads_Store:
        thread_S.start()

    '''序号重置'''
    #1等待请求页面队列为空，采集商品url线程退出
    while not pageQueue.empty():
        pass
    global PC_EXIT_FLAG
    PC_EXIT_FLAG = True
    for thread_CC in threads_crawlC:
        thread_CC.join()

    #1.1等待页面采集结果（商品url）队列为空，退出解析线程
    while not ComUrlQueue.empty():
        pass
    global PP_EXIT_FLAG
    PP_EXIT_FLAG = True
    for thread_PC in threads_parseC:
        thread_PC.join()

    #2等待url请求队列中为空，采集线程退出循环
    while not urlQueue.empty():
        pass
    global C_EXIT_FLAG
    C_EXIT_FLAG = True
    for thread_C in threads_crawl:
        thread_C.join()

    #2.1等待放置采集返回的商品详情页队列为空,则退出解析线程
    while not dataQueue.empty():
        pass
    global P_EXIT_FLAG
    P_EXIT_FLAG = True
    for thread_P in threads_parse:
        thread_P.join()

    #等待 已采集的商品数据队列为空，则退出存储入数据库的线程
    while not resQueue.empty():
        pass
    global S_EXIT_FLAG
    S_EXIT_FLAG = True
    for thread_S in threads_Store:
        thread_S.join()

if __name__ == '__main__':
    start = time.time()
    main()
    print('[INFO]耗时%s' % (time.time() - start))