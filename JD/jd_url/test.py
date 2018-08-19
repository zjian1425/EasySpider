#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/8/1 13:45
# @Author   : z_jian
# @contact  : zjian1425@gmail.com
# @File     : test.py

from selenium import webdriver
import time

opt = webdriver.ChromeOptions()
prefs = {
    'profile.default_content_setting_values': {
        'images': 2
    }
}
opt.add_experimental_option('prefs', prefs)
# chrome_options=opt
driver = webdriver.Chrome(chrome_options=opt)
driver.implicitly_wait(10)
driver.get('https://www.jd.com/')

driver.find_element_by_id('key').clear()
driver.find_element_by_id('key').send_keys('MO&CO')
time.sleep(2)
driver.find_element_by_css_selector('button.button').click()
time.sleep(2)

shop_name = driver.find_element_by_css_selector('li.gl-item:nth-child(1) div:nth-child(7) a').get_attribute('title')

if shop_name =='MO&Co.官方旗舰店':
    url = driver.find_element_by_css_selector('li.gl-item:nth-child(1) div:nth-child(7) a').get_attribute('href') # 新开一个网页
    driver.get(url)

#由于首页图片多，不禁止加载图片可能会加载没加载出allItem就运行下面一步了，导致定位不到元素
driver.get(driver.find_element_by_css_selector('a.allItem').get_attribute('href'))


pass





