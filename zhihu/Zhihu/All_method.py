#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/4/4 16:42
# @Author   : z_jian
# @contact  : zjian1425@gmail.com
# @File     : All_method.py
from urllib import parse
import requests
import json
import re
import pymysql

head = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
    'authorization': 'oauth c3cef7c66a1843f8b3a9e6a1e3160e20'
}


def urljoint1(url_token):  #个人主页连接拼接函数
    base = 'https://www.zhihu.com/people/'
    suff = '/activities'
    return (base +url_token + suff)

def urljoint2(url_token):    #获取用户关注的所有用户url_token的拼接函数
    base = 'https://www.zhihu.com/api/v4/members/'
    suff = '/followees?&limit=20&offset=0'
    return (base +url_token + suff)


def add_url_token(url_token):   #获取用户关注的所有用户url_token函数
    href = urljoint2(url_token)
    # 建立连接
    conn = pymysql.connect("localhost", "username", "password", "db_name", charset="utf8")
    # 设置游标
    cursor = conn.cursor()
    while True:
            jscontent = requests.get(href, headers=head).text
            try:#随机user-agent 会存在浏览器版本过低的情况，抓取的页面就不是json格式的文件了
                jsDict = json.loads(jscontent) #将爬取下来的json文件解码
                jsData = jsDict['data']
                if jsData:
                    # 调试后发现jsData列表中嵌套着字典，想法：通过一个for循环将列表中的每个字典中的url_token数据提取出来
                    i = 0
                    for each in jsData: #其实阈值控制是
                        # 将jiData列表转换为字典
                        dictionary = jsData[i]  # 先将每个item转换为单个的字典
                        if dictionary:
                            # list.append(dictionary["url_token"])  # 通过单个的字典取出url_token后面的参数，然后通过append函数添加在一个列表中
                            # 插入数据动作

                            do_insert = """insert into url_token_test(url_token)VALUES (%s)"""
                            try:
                                # 执行 -> 插入数据动作
                                cursor.execute(do_insert, (dictionary["url_token"]))
                                #保存操作
                                conn.commit()
                                i = i + 1
                            except:
                                i = i + 1 #跳过已存在的url_token
                                #在这一步可能存在爬取速度与插入速度不匹配造成异常退出
                                #如何解决
                                print("add_url_token已存在相同url_token")
                        else:
                            break
                else:
                    break
                href = (re.match(".*?\"next\": \"([a-zA-z]+:\/\/[^\s]*)\"\},.*", jscontent)).group(1)
            except:
                 break
    # return url_token_list #问题：担忧就是加入爬取的url_token非常大，可会会导致程序崩溃
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()

def get_urltoken_from_mysql():
    #与mysql建立连接
    conn = pymysql.connect("localhost","username","password","db_name",charset = "utf8")
    #设置游标
    cursor = conn.cursor()
    #查询动作
    do_select = """select url_token from url_token_test"""
    #执行查询动作
    cursor.execute(do_select)
    # 获取当前游标指向第一行数据
    url_token = cursor.fetchone()

    # 删除操作，删除id最小的哪一个
    do_delete = """delete from url_token_test order by id asc limit 1"""
    # 执行删除操作
    cursor.execute(do_delete)
    conn.commit()
    if url_token:   #若不空则返回
        return url_token
    else:   #若空则关闭与mysql的连接，返回none
        cursor.close()
        conn.close()
        return None
