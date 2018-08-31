#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Only.py
# @Author: zjian
# @Date  : 18-8-30
# @Contact  :zjian1425@gmail.com 
#@Software : PyCharm

#注意这里的Queue和多线程中的Queue不是同一个
from multiprocessing import Process,Queue,Pool
import time
from lxml import etree
from selenium import webdriver
from models.Setting import *
import os
import datetime
import pymysql

class insert(object):
    def __init__(self):
        self.conn = pymysql.connect(DB['host'], DB['username'], DB['password'], DB['db_name'], charset='utf8')
        self.cursor = self.conn.cursor()

    def execurl(self, item):
        do_insert = '''insert into only_veromoda_url(name,url,c_time)values (%s,%s,%s)'''
        self.cursor.execute(do_insert, item)
        self.conn.commit()

    def execcommodity(self,item):
        do_insert = '''insert into only_neromoda(url,title,goods,n_price,o_price,color,materials,brand,c_time)
        values (%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
        self.cursor.execute(do_insert, item)
        self.conn.commit()

    def __del__(self):
        self.cursor.close()
        self.conn.close()

def Parse(driver,url,num):
    '''
    先调用请求方法，下载源码，将源码利用xpath解析
    :return:
    '''
    DataQueue = Queue()
    brand ='only'
    c_time = datetime.datetime.now().strftime('%Y-%m-%d')
    print('[Parse] 进程号%s，父进程号%s' % (os.getpid(), os.getppid()))
    response = Requests(driver,url,num)
    response = etree.HTML(response)
    li_list = response.xpath('//*[@id="goodsListBox"]/li/a/@href')
    for li in li_list:
        suburl = 'https://www.only.cn/'+str(li) #check
        DataQueue.put((suburl,brand,c_time))

    #预留一个接口，直接抓取产品数据
    global  URLQueue
    URLQueue = DataQueue

    item_insert = insert()
    while not DataQueue.empty():
        item_insert.execurl(DataQueue.get(False))

def Requests(driver,url,num):
    '''
    启动selenium请求方法
    :param url:
    :param num:
    :return:
    '''
    print('[Requests] 进程号%s，父进程号%s'%(os.getpid(),os.getppid()))
    driver.get(url)
    if 'classifyIds' in url:
        driver.find_element_by_css_selector('.fist-nav li:nth-child(2)').click()
        driver.find_element_by_css_selector('#asideGoods li:nth-child({0}) div'.format(num)).click()
        driver.find_element_by_css_selector('#asideGoods li:nth-child({0}) ol li:nth-child(1)'.format(num)).click()
        driver.execute_script('window.scrollBy(0,1500)')
        while True:
            print('click')
            driver.find_element_by_css_selector('.water-bar').click()
            print('click')
            content = driver.page_source.encode('utf8','ignore')
            if b'\xe6\x9a\x82\xe6\x97\xa0\xe5\x95\x86\xe5\x93\x81' in content \
                    or \
                    b'\xe8\xaf\xa5\xe5\x95\x86\xe5\x93\x81\xe5\x85\xa8\xe9\x83' \
                    b'\xa8\xe5\x8a\xa0\xe8\xbd\xbd\xe5\xae\x8c\xe6\xaf\x95' in content:
                print('到底')
                break
            else:
                pass

    return driver.page_source

def OnlyCrawl(url,num):
    opt = webdriver.ChromeOptions()
    opt.add_experimental_option('prefs', Prefs)  # 从Setting中引用
    driver = webdriver.Chrome(chrome_options=opt)
    driver.implicitly_wait(10)  # 隐式等待10S
    print('[OnlyCrawl] 进程号%s，父进程号%s' % (os.getpid(), os.getppid()))
    Parse(driver,url,num)
    driver.close()

def Omain():
    '''# suburlQueue = Queue()#创建队列，保存各进程获取suburl
    #
    # Process_list = []
    # for num in only_num:    #各进程所点击的第几个数列表
    #     P = Only(suburlQueue,O_start_url,num)
    #     Process_list.append(P)
    # for P in Process_list:
    #     P.start()
    #
    # for P in Process_list:# 让主进程等待子进程执行完成
    #     P.join()
    # while not suburlQueue.empty():
    #     urlQueue.put(suburlQueue.get())'''
    # 开启四个进程，即同事打开4个谷歌浏览器抓取
    pool = Pool(processes=2)
    print('[Omain] 进程号%s，父进程号%s' % (os.getpid(), os.getppid()))
    for i in only_num:
        try:
            pool.apply_async(OnlyCrawl,(O_start_url,i))
        except Exception as e:
            print(e)
    pool.close()
    pool.join()
    print('urlcrawl is done')

def ParseCommodity(page_source,url):
    response = etree.HTML(page_source)
    brand = 'only'
    title = response.xpath('/html/body/div[2]/div[2]/div/div[3]/h3/span[1]/text()')[0]
    goods_num = response.xpath('/html/body/div[2]/div[2]/div/div[3]/p[1]/span/text()')[0]
    n_price = response.xpath('/html/body/div[2]/div[2]/div/div[3]/p[2]/strong/text()')[0]
    o_price = response.xpath('/html/body/div[2]/div[2]/div/div[3]/p[2]/span[2]/text()')[0]
    color = ','.join(response.xpath('//*[@id="colors"]/li/text()'))
    materials = response.xpath('//*[@id="goods-infos"]/text()')[0]
    Insert = insert()
    c_time = datetime.datetime.now().strftime('%Y-%m-%d')
    item = (url,title, goods_num, n_price, o_price, color,materials,brand,c_time)
    Insert.execcommodity(item)

def CrawlCommodity(url):
    opt = webdriver.ChromeOptions()
    opt.add_experimental_option('prefs', Prefs)  # 从Setting中引用
    driver = webdriver.Chrome(chrome_options=opt)
    driver.implicitly_wait(10)  # 隐式等待10S
    driver.get(url)
    driver.execute_script('window.scrollBy(0,3000)')
    driver.execute_script('window.scrollBy(0,4000)')
    ParseCommodity(driver.page_source.encode('utf8','ignore'),url)
    driver.close()

if __name__ =='__main__':
    print('[main] 进程号%s，父进程号%s' % (os.getpid(), os.getppid()))
    start = time.time()
    Omain()
    print('[INFO] 耗时%s：'%(time.time()-start))
    '''
    开始抓取商品详情
    '''
    pool = Pool(processes=4)
    while not URLQueue.empty():
        url = URLQueue.get(False)
        pool.apply_async(CrawlCommodity, args=(url,))
    pool.close()
    pool.join()
    print('Commodity is done')
