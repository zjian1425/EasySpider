#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Spider.py
# @Author: zjian
# @Date  : 18-8-24
# @Contact  :zjian1425@gmail.com 
#@Software : PyCharm

__doc__ = '''请求数据模块'''


import requests
from queue import *
import threading
import time
from lxml import etree

class HstyleSpider(threading.Thread):

    def __init__(self, url, q):
        super(HstyleSpider, self).__init__()
        self.url = url
        self.q = q
        self.header = {
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36',
        }

    def run(self):
        self.parse_page()

    def send_request(self,url):
        i = 0
        while i<3:
            try:
                print(u'[INFO]请求url:%s'%url)
                html = requests.get(url=url,headers=self.header).content
            except Exception as e:
                print(u'[INFO] %s%s'%(e,url))
                i+=1
                time.sleep(3)
            else:
                return html

    def parse_page(self):
        """
        解析网站源码，并采用ｘｐａｔｈ选择器提取 目标字段
        :return:
        """
        response =self.send_request(self.url)
        response = etree.HTML(response)
        # title = response.xpath('//*[@id="goods_detail_1"]/h1/text()')
        title = ''.join(response.xpath('//*[@id="goods_detail_1"]/h1/text()')).strip()
        try:
            bd = response.xpath('//*[@id="goods_detail_1"]/h1/em/a/span/text()')[0]
        except:
            bd =''
        goods_nums = response.xpath('//*[@id="goods_detail_1"]/ul/li[1]/span[1]/text()')[0]  # 商品货号
        o_price = response.xpath('//*[@id="goods_detail_1"]/ul/li[1]/del/text()')[0]
        n_price = response.xpath('//*[@id="goods_detail_1"]/ul/li[2]/em/text()')[0]
        sale_count = response.xpath('//*[@id="goods_detail_1"]/ul/li[3]/span/text()')[0]
        comment_nums = response.xpath('//*[@id="goods_detail_1"]/ul/li[4]/span[2]/a/text()')[0]
        score = response.xpath('//*[@id="goods_detail_1"]/ul/li[4]/span[1]/em/@title')[0]
        brand = response.xpath('//*[@id="J_attrBrandName"]/text()')[0]
        c_size = response.xpath('//*[@id="J_AttrUL"]/li[3]/text()')[0].replace('\n', '').replace(' ','').replace('\xa0', ',')
        color = response.xpath('//*[@id="J_AttrUL"]/li[4]/text()')[0].replace('\n', '').replace(' ','').replace('\xa0', ',')

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
        self.q.put(item)

def main():
    # 创建一个queue 用于获取请求后返回的数据
    q = Queue()

    #请求url列表
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

    #保存线程
    threads = []

    for url in url_list:
        p = HstyleSpider(url,q)
        threads.append(p)

    for thread in threads:
        thread.start()


    for thread in threads:
        thread.join()


    # while not q.empty():
    #     print(q.get())


if __name__=="__main__":

    start = time.time()
    main()
    print(('[info]耗时：%s'%(time.time()-start)))