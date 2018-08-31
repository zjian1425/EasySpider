#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Veromoda.py
# @Author: zjian
# @Date  : 18-8-30
# @Contact  :zjian1425@gmail.com 
#@Software : PyCharm

from multiprocessing import Process,Queue   #注意这里的Queue和多线程中的Queue不是同一个
import time
from  lxml import etree
from selenium import webdriver
from models.Setting import *

class Veromoda(Process):

    def __init__(self, queue, url, num):
        super(Veromoda, self).__init__()
        self.queue = queue
        self.url = url
        self.num = num
        opt = webdriver.ChromeOptions()
        opt.add_experimental_option('prefs', Prefs)  # 从Setting中引用
        self.driver = webdriver.Chrome(chrome_options=opt)
        self.driver.implicitly_wait(10)  # 隐式等待10S

    def run(self):
        self.parse()

    def requests(self, url, num):
        '''
        启动selenium请求方法
        :param url:
        :param num:
        :return:
        '''
        self.driver.get(url)
        if 'classifyIds' in url:
            self.driver.find_element_by_css_selector('.fist-nav li:nth-child(2)').click()
            self.driver.find_element_by_css_selector('#asideGoods li:nth-child({0}) div'.format(num)).click()
            self.driver.find_element_by_css_selector('#asideGoods li:nth-child({0}) ol li:nth-child(1)').click()
            self.driver.execute_script('window.scrollBy(0,1500)')
            time.sleep(0.5)

            while True:
                self.driver.find_element_by_css_selector('water-bar').click()
                content = self.driver.page_source.encode('utf8', 'ignore')
                if b'\xe6\x9a\x82\xe6\x97\xa0\xe5\x95\x86\xe5\x93\x81' in content \
                        or \
                        b'\xe8\xaf\xa5\xe5\x95\x86\xe5\x93\x81\xe5\x85\xa8\xe9\x83' \
                        b'\xa8\xe5\x8a\xa0\xe8\xbd\xbd\xe5\xae\x8c\xe6\xaf\x95' in content:
                    break
                else:
                    time.sleep(1)

        return self.driver.page_source

    def parse(self):
        '''
        先调用请求方法，下载源码，将源码利用xpath解析
        :return:
        '''
        response = self.requests(self.url, self.num)
        response = etree.HTML(response)
        li_list = response.xpath('//*[@id="goodsListBox"]/li/a/@href')
        for li in li_list:
            suburl = 'https://www.only.cn/' + str(li.root)  # check
            self.queue.put([suburl,'veromoda'])

    def __del__(self):
        # 当前进程结束时，浏览器退出
        self.driver.quit()

def Vmain(urlQueue):
    # 创建队列，保存各进程获取suburl
    suburlQueue = Queue()
    Process_list = []
    for num in veromoda_num:
        P = Veromoda(suburlQueue,V_start_url,num)
        Process_list.append(P)

    for P in Process_list:
        P.start()

    for P in Process_list:
        P.join()

    while not suburlQueue.empty():
        urlQueue.put(suburlQueue.get())