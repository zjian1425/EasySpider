#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/4/10 12:53
# @Author   : z_jian
# @contact  : zjian1425@gmail.com
# @File     : create_tables.py
import pymysql
def operate_mysql():

    conn = pymysql.connect("localhost","username","password","db_name",charset = "utf8")

    cursor = conn.cursor()

    do_create_users_info = """CREATE TABLE users_info (
                        url_token varchar(100) NOT NULL,
                       u_name varchar(300) NOT NULL,
                       follwingCount varchar(11) DEFAULT '0',
                       followerCount varchar(11) DEFAULT '0',
                       asks varchar(11) DEFAULT '0',
                       answerCount varchar(11) DEFAULT '0',
                       gender varchar(11) DEFAULT '-1',
                       edu varchar(500) DEFAULT NULL,
                       job varchar(500) DEFAULT NULL,
                       place varchar(500) DEFAULT NULL,
                       introduce TEXT,
                       PRIMARY KEY (url_token)
                       ) ENGINE=InnoDB DEFAULT CHARSET=utf8"""

    cursor.execute("drop table if exists users_info")

    cursor.execute(do_create_users_info)

    conn.commit()

    #其中url_token字段是主键，而id字段则是自增字段。
    do_create_url_token = """create table url_token (id int auto_increment,
                              url_token varchar(20) primary key,key(id))"""

    cursor.execute("drop table if exists url_token")
    #实现id自增且不是主键
    cursor.execute(do_create_url_token)

    conn.commit()

    cursor.close()

    conn.close()