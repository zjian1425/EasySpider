# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from scrapy.http import HtmlResponse

class JdUrlSpiderMiddleware(object):
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


class JdUrlDownloaderMiddleware(object):
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

import random
import time

class NewDownloaderMiddleware(object):

    def process_request(self, request, spider):
        if spider.count ==1:

            spider.count +=1

            spider.driver.get(request.url)
            spider.driver.find_element_by_id('key').clear()
            spider.driver.find_element_by_id('key').send_keys('MO&CO')
            time.sleep(2)
            spider.driver.find_element_by_css_selector('button.button').click()
            time.sleep(2)

            shop_name = spider.driver.find_element_by_css_selector('li.gl-item:nth-child(1) div:nth-child(7) a').get_attribute('title')

            if shop_name == 'MO&Co.官方旗舰店':
                url = spider.driver.find_element_by_css_selector('li.gl-item:nth-child(1) div:nth-child(7) a').get_attribute('href')  # 新开一个网页
                spider.driver.get(url)

            # 由于首页图片多，不禁止加载图片可能会加载没加载出allItem就运行下面一步了，导致定位不到元素
                spider.driver.get(spider.driver.find_element_by_css_selector('a.allItem').get_attribute('href'))

        elif spider.count>1:

            time.sleep(self.wait_time())
            spider.driver.get(request.url)
            spider.driver.execute_script("window.scrollBy(0,{0})".format(self.random_scroll_lenth()))
            time.sleep(self.wait_time())
            spider.driver.execute_script("window.scrollBy(0,{0})".format(self.random_scroll_lenth()))
            time.sleep(self.wait_time())
            spider.driver.execute_script("window.scrollBy(0,{0})".format(self.random_scroll_lenth()))

        content = spider.driver.page_source.encode('utf8', 'ignore')

        return HtmlResponse(spider.driver.current_url, encoding='utf8', body=content, request=request)

    def wait_time(self):

        t3 = random.uniform(1,3)
        print('等待时间:{0}'.format(t3))
        return t3


    def random_scroll_lenth(self):

        length = random.uniform(300,2000)
        print('下拉距离为：{0}'.format(length))
        return length
