#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/6/11 16:54
# @Author   : z_jian
# @contact  : zjian1425@gmail.com
# @File     : ip_poolstore.py

import requests
import random
import pymysql
import time

  class store_ip():

    def __init__(self):
        self.conn = pymysql.connect('xxxxx','xxx','xxxx','xxxxxx',charset = 'utf8')
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.commit()
        print('IP线程池添加成功')
        self.cursor.close()
        self.conn.close()

    def execute_query(self,data_list):
        sumeffect =0
        for i in data_list:
            query = """insert into  Ip_proxy(ip_port) values ('{0}')""".format(i)
            roweffect = self.cursor.execute(query)
            sumeffect +=roweffect
        return sumeffect

    def Random_UA(self):
        USER_AGENTS = [
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
        "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
        "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
        "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52", ]
        return random.choice(USER_AGENTS)

def main():
    url = 'http://162430100079702367.s.y2000.com.cn/?num=5000&scheme=1&anonymity=3'
    conn = store_ip()
    user_agent = {
        'headers': conn.Random_UA()
    }
    a = requests.get(url,headers = user_agent).content
    a = str(a)
    ip_list = a.split('\\r\\n')
    ip_list[0]=ip_list[0].strip('b\'')
    ip_list[len(ip_list)-1] = ip_list[len(ip_list)-1].strip('\'')
    conn.execute_query(ip_list)

if __name__ == '__main__':
    cnt = 0
    while cnt<2000:
        main()
        cnt +=1
        time.sleep(0.5)