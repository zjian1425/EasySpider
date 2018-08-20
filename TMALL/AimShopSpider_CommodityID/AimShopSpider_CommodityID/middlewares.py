# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

import time
import random

from scrapy import signals
from scrapy.http import HtmlResponse
import time

class AimshopspiderCommodityidSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class AimshopspiderCommodityidDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


from AimShopSpider_CommodityID.settings import account as act
class SeleniumFirefoxRenderAjaxDownloaderMiddleware(object):

    account = act #用于判断是否已经登录
    #思想是控制在同一个session中抓取数据
    def process_request(self,request,spider):

        #这里需要注意的一点是可以通过if 判断spider.name或者request.url(正则匹配)来处理
        #需要用到selenium加载动态网页的爬虫或者url，这样就不用使用selenium去动态加载每一个页面了

        print('start request')
        flag = 0 #判断死循环跳出标志

        '''猜想：这一步操作是否可以放置在process_response中去控制'''
        while True:
            spider.driver.get(request.url)

            spider.driver.execute_script("window.scrollBy(0,{0})".format(self.random_scroll_lenth()))
            time.sleep(self.wait_time())
            spider.driver.execute_script("window.scrollBy(0,{0})".format(self.random_scroll_lenth()))
            time.sleep(self.wait_time())
            spider.driver.execute_script("window.scrollBy(0,{0})".format(self.random_scroll_lenth()))

            content = spider.driver.page_source.encode('utf8','ignore')
            if self.account in str(content): #条件
                print('ready to return HtmlRespnse!')
                flag += 1
                break #知道成功才退出循环
            else:
                time.sleep(20) #登录帐号
                '''这里最好能实现自动登录利用selenium'''
                '''手动操作：刷二维码（有可能需要两次）'''
                #第一次扫描二维码点击确认登录后浏览器上方的地址栏会跳出拦截重定向的提示，在扫描一次就不会出现这样的
                # 问题，即成功登录淘宝

        return HtmlResponse(spider.driver.current_url, encoding='utf8', body=content, request=request)


    def wait_time(self):

        t3 = random.uniform(1,2)
        print('页面下拉等待时间:{0}'.format(t3))
        return t3


    def random_scroll_lenth(self):

        length = random.uniform(500,3000)
        print('当前页面下拉距离为：{0}'.format(length))
        return length
