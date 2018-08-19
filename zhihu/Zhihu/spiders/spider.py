#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/4/4 16:17
# @Author   : z_jian
# @contact  : zjian1425@gmail.com
# @File     : spider.py

import scrapy
import sys
import re
from scrapy.http import Request
from Zhihu.All_method import urljoint1
from Zhihu.items import ZhihuItem
from Zhihu.All_method import get_urltoken_from_mysql
from selenium import webdriver
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from scrapy import  signals
from scrapy.xlib.pydispatch import dispatcher
from Zhihu.Random_User_Agent import ret_UA


class ZhihuSpider(scrapy.Spider):
    name = 'Zhihu'
    allowed_domains = ['www.zhihu.com']
    key = get_urltoken_from_mysql()
    if key:
        start_urls = [urljoint1("".join(key))]
    else:
        print("表空")
        sys.exit() #退出

    def __init__(self):
        # 禁止加载图片，提升爬取速度
        opt = webdriver.ChromeOptions()
        prefs = {
            'profile.default_content_setting_values': {
                'images': 2
            }
        }
        opt.add_experimental_option('prefs', prefs)
        ua = ret_UA()
        opt.add_argument('user-agent=ua')
        self.browser = webdriver.Chrome(chrome_options=opt)
        self.browser.implicitly_wait(5)

        super(ZhihuSpider,self).__init__()
        #向CloseSpider方法发送爬虫结束信号，准备关闭pthantomjs浏览器
        dispatcher.connect(self.CloseSpider,signals.spider_closed)

    def CloseSpider(self,spider):
        print("spider closed")
        #当爬虫结束时关闭浏览器
        self.browser.quit()

    def parse(self, response):
        while True:
            tuple_value = get_urltoken_from_mysql()
            if tuple_value:
                url_token = "".join(tuple_value)  # 调用函数从数据库中返回一个url_token
                next_user_url = urljoint1(url_token)
                yield Request(url =next_user_url,meta={"url_token":url_token},callback=self.parse_detail)
            #yield就是return 返回一个值，并且记住这个返回的位置，下次迭代就从这个位置后(下一行)开始。
            else:
                sys.exit()
                print("url_token_test表空，程序等待结束")
    def parse_detail(self, response):
            list_Label = response.css(".ProfileHeader-detailLabel::text").extract()
            # 行业和个人简介
            business_introduce = response.css(".ProfileHeader-detailValue::text").extract()
            introduce=''
            if len(business_introduce) == 2:
                business = business_introduce[0]
                introduce = business_introduce[1]
                list_Label.remove('所在行业')
                list_Label.remove('个人简介')
            elif len(business_introduce) == 1:
                for i in list_Label:
                    if i == '所在行业':
                        business = business_introduce[0]
                        introduce = ''
                        list_Label.remove('所在行业')
                    elif i == '个人简介':
                        business = ''
                        introduce = business_introduce[0]
                        list_Label.remove('个人简介')
                        break
            else:
                business = ''
                introduce = ''
            # 所在地
            place = response.css("div.ProfileHeader-detailValue span:nth-child(1)::text").extract()
            list_data = response.css(
                "div.ProfileHeader-detailValue div.ProfileHeader-field:nth-child(1)::text").extract()
            # 职位
            job = ''
            # 学校
            edu = ''
            if len(list_data) == 2:
                job = list_data[0]
                edu = list_data[1]
            elif len(list_data) == 1:
                for i in list_Label:
                    if i == '职业经历':
                        job = list_data[0]
                    elif i == '教育经历':
                        edu = list_data[0]
            elif len(list_data) == 0:
                job = ''
                edu = ''
            else:
                print("异常")
            # 数据清洗
            if place:
                place = "".join(place)
                place = place.replace("现居", "")
            else:
                place = "".join(place)
            # 性别
            gender = response.css("meta[itemprop*='gender']::attr(content)").extract()
            if gender:
                if gender[0] == 'Male':
                    gender = 0  # 0->male
                else:
                    gender = 1  # 1->female
            else:
                gender = -1  # -1未知
            # 名称
            u_name = response.css("span.ProfileHeader-name::text").extract_first()

            # 回答数
            answerCount = response.css("li[aria-controls*='Profile-answers'] a span::text").extract_first()
            # 被关注数
            followerCount = response.css("meta[itemprop*='followerCount']::attr(content)").extract_first()
            # 提问数
            asks = response.css("li[aria-controls*='Profile-asks'] a span::text").extract_first()
            # 关注数
            content = str(response.body)
            re_match = re.match(".*?<.*?title=\"(\d*)\">.*</strong>", content)
            if re_match:
                follwingCount = re_match.group(1)
            else:
                follwingCount = 0
            url_token = response.meta['url_token']
            # ZhihuItem类实例化Zhihu_item
            Zhihu_item = ZhihuItem()
            Zhihu_item["u_name"] = u_name  # 1用户名称
            Zhihu_item["follwingCount"] = follwingCount  # 2用户关注的人数量
            Zhihu_item["followerCount"] = followerCount  # 3关注用户的人的数量
            Zhihu_item["gender"] = gender  # 4性别
            Zhihu_item["edu"] = edu  # 5教育经历
            Zhihu_item["job"] = job # 6职业经历
            Zhihu_item["place"] = place  # 7居住地列表
            Zhihu_item["url_token"] = [url_token] #8 关键字
            Zhihu_item["asks"] = asks  # 9提问数
            Zhihu_item["answerCount"] = answerCount  # 10回答数
            Zhihu_item["introduce"] = introduce #11回答数
            # item值填充
            yield Zhihu_item








        # content = response.css("div#data").extract_first()
        # try:
        #     with open("D:\github_local_repository\zjan_repository\crawler_project\zjan\info.html","wb") as file1:
        #         file1.write(content.encode("utf-8"))
        #     file1.close()
        # except:
        #     print("parse_detail 版本过低")
        #     return self.parse()
        #
        # # 1用户头像url
        # img_url = response.css(".UserAvatar-inner::attr(src)").extract_first()
        # # 2用户名称 css选择器
        # user_name = response.css( "html body.Entry-body div#root div main.App-main div div div#ProfileHeader.ProfileHeader div.Card div.ProfileHeader-wrapper div.ProfileHeader-main div.ProfileHeader-content div.ProfileHeader-contentHead h1.ProfileHeader-title span.ProfileHeader-name::text").extract_first("")
        #              # 2.从抓取的文件中用正则表达式提取出我们关注的数据
        # fgC_re = re.match(".*\"followingCount\":(\d*),.*",content)
        # if fgC_re:
        #     # 4用户关注的人数量
        #     user_followingCount = int(fgC_re.group(1))
        # else:
        #     user_followingCount = 0
        #
        # frC_re = re.match(".*\"followerCount\":(\d*),\"employments\".*",content)
        # if frC_re:
        #     # 5关注用户的人的数量
        #     user_followerCount = int(frC_re.group(1))
        # else:
        #     user_followerCount = 0
        # pinsCount = re.match(".*\"pinsCount\":(\d*),.*",content)
        # if pinsCount:
        #     # 6想法
        #     idea_num = int(pinsCount.group(1))
        # else:
        #     idea_num = 0
        #
        # sex = re.match(".*\"gender\":(\d*),.*",content)
        # if sex:
        #     # 7性别
        #     gender = int (sex.group(1)) #   1->男；0->女
        # else:
        #     gender = -1     #-1为未知
        #
        # favorC = re.match(".*\"favoriteCount\":(\d*),.*",content)
        # if favorC:
        #     # 8用户收藏数量
        #     favoriteCount = int (favorC.group(1))
        # else:
        #     favoriteCount = 0
        #
        # vc = re.match(".*\"voteupCount\":(\d*),\"commercialQuestionCount\".*",content)
        # if vc:
        #     # 9获得的赞
        #     voteupCount = int (vc.group(1))
        # else:
        #     voteupCount = 0
        #
        # fcc = re.match(".*\"followingColumnsCount\":([a-z0-9]*),.*",content)
        # if fcc:
        #     # 10关注的专栏数量
        #     followingColumnsCount = int(fcc.group(1))
        # else:
        #     followingColumnsCount = 0
        #
        # plc = re.match(".*\"participatedLiveCount\":([a-z0-9]*),.*",content)
        # if plc:
        #     # 11参加的live数量
        #     participatedLiveCount = int(plc.group(1))
        # else:
        #     participatedLiveCount = 0
        #
        # fflc = re.match(".*\"followingFavlistsCount\":([a-z0-9]*),.*",content)
        # if fflc:
        #     # 12关注的收藏夹
        #     followingFavlistsCount = int (fflc.group(1))
        # else:
        #     followingFavlistsCount = 0
        #
        # fc = re.match(".*\"favoritedCount\":([a-z0-9]*),.*",content)
        # if fc:
        #     # 13用户的观点或文章被收藏数
        #     favoritedCount = int (fc.group(1))
        # else:
        #     favoritedCount = 0
        #
        # id = re.match(".*\"isForceRenamed\":false,\"id\":\"(.{32})\",.*",content)
        # if id:
        #     #14用户id
        #     uid = id.group(1)
        # else:
        #     uid = ''
        # #15学校列表
        # school_list = [] #由于可能教育经历不止一个，所以做一个循环
        # while True:         #由于正则匹配默认是贪婪匹配
        #                      # .*?为固定搭配 -->非贪婪匹配
        #     sch = re.match(".*?\"school\":.*?\"name\":\"([\u4e00-\u9fa5]*[a-z0-9]*|[a-z0-9]*)\"",content)
        #     if sch:
        #         school_list.append(sch.group(1))
        #         content = content.replace("school","学校",1)
        #     else:
        #         break
        # i = ',' #将列表装换成字符串
        # school_list = i.join(school_list)
        # # 16工作列表
        # job_list = []
        # while True:
        #     job = re.match(".*?\"job\":.*?\"name\":\"([\u4e00-\u9fa5]*[a-z0-9]*|[a-z0-9]*)\"",content)
        #     if job:
        #         job_list.append(job.group(1))
        #         content = content.replace("job","工作",1)
        #     else:
        #         break
        # # 将列表装换成字符串
        # job_list = i.join(job_list)
        # # 17居住地列表
        # place_list = []
        # while True:
        #     place = re.match(".*?\"locations\":\[\{\"introduction\".*?\"name\":\"([\u4e00-\u9fa5]*[a-z0-9]*|[a-z0-9]*)\",.*?\}\],", content)
        #     if place:
        #         place_list.append(place.group(1))
        #         content = content.replace("locations", "名称", 1)
        #     else:
        #         break
        # # 将列表装换成字符串
        # place_list = i.join(place_list)
        # #18所学专业列表
        # major_list = []
        # while True:                                                                      #加.*{最少，最多}要留意中间有其他字符的情况
        #     major = re.match(".*?\"educations\":\[\{.*?\"major\":.*?\"name\":(\"[\u4e00-\u9fa5]*.{0,5}[a-z]*|.{0,5}[a-z]*\")\",.*?\}?,", content)
        #     if major:
        #         major_list.append(major.group(1))
        #         content = content.replace("major","专业",1)
        #     else:
        #         break
        # # 将列表装换成字符串
        # major_list = i.join(major_list)
        # #19公司列表
        # company_list = []
        # while True:
        #     compy = re.match(".*?\"company\":.*?\"name\":\"([\u4e00-\u9fa5]*[a-z0-9]*|[a-z0-9]*)\"",content)
        #     if compy:
        #         company_list.append(compy.group(1))
        #         content = content.replace("company","公司",1)
        #     else:
        #         break
        #   # 将列表装换成字符串
        # company_list = i.join(company_list)
        # url_token = response.meta['url_token']

