# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals


class VeromodaSpiderMiddleware(object):
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


class VeromodaDownloaderMiddleware(object):
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

from scrapy.http import HtmlResponse
import time
class NewDownloaderMiddleware(object):

    def process_request(self, request, spider):

        spider.driver.get(request.url)
        if spider.count ==0:
            spider.driver.find_element_by_css_selector('.fist-nav li:nth-child(2)').click()
            spider.driver.find_element_by_css_selector('#asideGoods li:nth-child(16) div').click()
            spider.driver.find_element_by_css_selector('#asideGoods li:nth-child(16) ol li:nth-child(1)').click()
            spider.driver.execute_script('window.scrollBy(0,1500)')
            time.sleep(0.5)
            # spider.driver.find_element_by_css_selector('.all-goods-list li:nth-child(16) ol li:nth-child(1)').click()
            # spider.driver.implicitly_wait(10)
            while True:
                spider.driver.find_element_by_css_selector('.water-bar').click()

                content = spider.driver.page_source.encode('utf8','ignore')
                if b'\xe6\x9a\x82\xe6\x97\xa0\xe5\x95\x86\xe5\x93\x81'  in content \
                        or \
                        b'\xe8\xaf\xa5\xe5\x95\x86\xe5\x93\x81\xe5\x85\xa8\xe9\x83' \
                           b'\xa8\xe5\x8a\xa0\xe8\xbd\xbd\xe5\xae\x8c\xe6\xaf\x95' in content:
                    break
                else:
                    time.sleep(1)
            spider.count +=1
            return HtmlResponse(spider.driver.current_url, encoding='utf8', body=content, request=request)

        else:
            spider.driver.execute_script('window.scrollBy(0,3000)')
            spider.driver.execute_script('window.scrollBy(0,4000)')
            content = spider.driver.page_source.encode('utf8', 'ignore')
            return HtmlResponse(spider.driver.current_url,encoding='utf8',body=content,request=request)