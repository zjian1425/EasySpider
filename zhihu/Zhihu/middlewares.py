# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
from fake_useragent import UserAgent
from scrapy import signals
from selenium import webdriver
import time
from scrapy.http import HtmlResponse

class ZhihuSpiderMiddleware(object):
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

class ZhihuDownloaderMiddleware(object):
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

class RondomUserAgentMiddleware(object):
    #发起requests时随机更换User-Agent
    def __init__(self,crawler):
        super(RondomUserAgentMiddleware,self).__init__()
        self.ua = UserAgent()#实例化对象
    @classmethod #不需要实例化，cls直接可以调用类对象
    def from_crawler(cls,crawler):
         return cls(crawler)

    def process_request(self, request, spider):
        random_useragent = self.ua.random
        request.headers.setdefault('User-Agent',self.ua.random)

class PhantomjsMiddleware(object):
    def process_request(self,request,spider):
        if spider.name=="Zhihu":
            print("执行渲染")
            spider.browser.get(request.url)
            spider.browser.implicitly_wait(5)
            print("请求已发送")
            try:
                spider.browser.find_element_by_xpath("//button[contains(@class,'ProfileHeader-expandButton')]").click()
                spider.browser.implicitly_wait(5)
            except:
                print("找不到点击键")
            print("获取网页源码")
            content = spider.browser.page_source.encode("utf-8", "ignore")
            print("访问" + request.url)
            time.sleep(0.5)
            #返回
            return HtmlResponse(spider.browser.current_url, encoding='utf-8', body=content, request=request)
        else:
            return None
