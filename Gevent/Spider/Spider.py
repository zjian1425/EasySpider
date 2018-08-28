#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Spider.py
# @Author: zjian
# @Date  : 18-8-27
# @Contact  :zjian1425@gmail.com 
#@Software : PyCharm



#!/usr/bin/env python2
# -*- coding=utf-8 -*-

from queue import Queue
import time
from lxml import etree
import requests
import gevent

#　打上猴子补丁
from gevent import monkey
monkey.patch_all()

class HstyleSpider(object):
    def __init__(self):
        # 创建一个队列用来保存进程获取到的数据
        self.q = Queue()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36',
        }

    def run(self,url):
        self.parse_page(url)

    def send_request(self,url):
        '''
        用来发送请求的方法
        :return: 返回网页源码
        '''
        # 请求出错时，重复请求３次,
        i = 0
        while i <= 3:
            try:
                print (u"[INFO]请求url:"+url)
                html = requests.get(url=url,headers=self.headers).content
            except Exception as e:
                print (u'[INFO] %s%s'% (e,url))
                i += 1
            else:
                return html

    def parse_page(self,url):
        '''
        解析网站源码，并采用ｘｐａｔｈ提取　电影名称和平分放到队列中
        :return:
        '''
        response = self.send_request(url)
        response = etree.HTML(response)
        # title = response.xpath('//*[@id="goods_detail_1"]/h1/text()')
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
        self.q.put(item)


    def main(self):


        # base_url = 'https://movie.douban.com/top250?start='
        # # 构造所有ｕｒｌ
        # url_list = [base_url+str(num) for num in range(0,225+1,25)]

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
                    'http://www.handu.com/goods-1064926.html']

        # 创建协程并执行
        job_list = [gevent.spawn(self.run,url) for url in url_list]
        # 让线程等待所有任务完成，再继续执行。
        gevent.joinall(job_list)

        while not self.q.empty():
            print (self.q.get())

if __name__=="__main__":
    start = time.time()
    Hstyle = HstyleSpider()
    Hstyle.main()
    print ('[info]耗时：%s'%(time.time()-start))

# gevent