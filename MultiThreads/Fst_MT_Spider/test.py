#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test.py
# @Author: zjian
# @Date  : 18-8-26
# @Contact  :zjian1425@gmail.com 
#@Software : PyCharm
#
# headers = {
#             'Cookie': 'bid=baCNN3pAFyQ; ap_v=1,6.0; __utma=30149280.1716163472.1535286855.1535286855.1535286855.1; __utmc=30149280; __utmz=30149280.1535286855.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
#             'Host': 'fundin.douban.com',
#             'Referer': 'https://movie.douban.com/top250?start=0',
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36',
#         }
# import requests
# a = requests.get('https://movie.douban.com/top250?start=0',headers=headers)
# pass


class animals(object):

    def __init__(self, sort, features):
        self.sort = sort
        self.features = features

    def sports(self):
        print('[info] %s'%self.features)

    def eat(self):
        print('[info] %s'%self.sort)

class dog(animals):
    def __init__(self, meat, run,name,max_age):
        super(dog, self).__init__(meat,run)
        self.name = name
        self.max_age = max_age



if __name__=='__main__':
    hsq = dog('poke','fast','hsq',4)
    hsq.sports()
    hsq.eat()



    # url_list = ['http://www.handu.com/goods-1073166.html',
    #             'http://www.handu.com/goods-1072736.html',
    #             'http://www.handu.com/goods-1072705.html',
    #             'http://www.handu.com/goods-1072183.html',
    #             'http://www.handu.com/goods-1072173.html',
    #             'http://www.handu.com/goods-1070243.html',
    #             'http://www.handu.com/goods-1069943.html',
    #             'http://www.handu.com/goods-1068374.html',
    #             'http://www.handu.com/goods-1068374.html',
    #             'http://www.handu.com/goods-1068342.html',
    #             'http://www.handu.com/goods-1066902.html',
    #             'http://www.handu.com/goods-1065701.html',
    #             'http://www.handu.com/goods-1065372.html',
    #             'http://www.handu.com/goods-1064926.html',
    #             'http://www.handu.com/goods-1074042.html',
    #             'http://www.handu.com/goods-1074019.html',
    #             'http://www.handu.com/goods-1074003.html',
    #             'http://www.handu.com/goods-1074004.html',
    #             'http://www.handu.com/goods-1074001.html',
    #             'http://www.handu.com/goods-1073990.html',
    #             'http://www.handu.com/goods-1073904.html',
    #             'http://www.handu.com/goods-1073867.html',
    #             'http://www.handu.com/goods-1073866.html',
    #             'http://www.handu.com/goods-1073854.html',
    #             'http://www.handu.com/goods-1073853.html',
    #             'http://www.handu.com/goods-1073846.html',
    #             'http://www.handu.com/goods-1073846.html',
    #             'http://www.handu.com/goods-1073845.html',
    #             'http://www.handu.com/goods-1073831.html',
    #             'http://www.handu.com/goods-1073825.html',
    #             'http://www.handu.com/goods-1073823.html',
    #             'http://www.handu.com/goods-1073822.html',
    #             'http://www.handu.com/goods-1073814.html',
    #             'http://www.handu.com/goods-1073813.html',
    #             'http://www.handu.com/goods-1073812.html',
    #             'http://www.handu.com/goods-1073807.html',
    #             'http://www.handu.com/goods-1073804.html',
    #             'http://www.handu.com/goods-1073783.html',
    #             'http://www.handu.com/goods-1073756.html',
    #             'http://www.handu.com/goods-1073746.html',
    #             'http://www.handu.com/goods-1073751.html',
    #             'http://www.handu.com/goods-1073744.html',
    #             'http://www.handu.com/goods-1073737.html',
    #             'http://www.handu.com/goods-1073714.html',
    #             'http://www.handu.com/goods-1073672.html',
    #             'http://www.handu.com/goods-1073638.html']
    # # 将url添加进Queue
    # for url in url_list:
    #     urlQueue.put(url)