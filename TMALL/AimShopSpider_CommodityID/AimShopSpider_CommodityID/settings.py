# -*- coding: utf-8 -*-

# Scrapy settings for AimShopSpider_CommodityID project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'AimShopSpider_CommodityID'

SPIDER_MODULES = ['AimShopSpider_CommodityID.spiders']
NEWSPIDER_MODULE = 'AimShopSpider_CommodityID.spiders'

# '''load module of the multi-spider's commands'''
# COMMANDS_MODULE = 'AimShopSpider_CommodityID.commands'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'AimShopSpider_CommodityID (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'AimShopSpider_CommodityID.middlewares.AimshopspiderCommodityidSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'AimShopSpider_CommodityID.middlewares.AimshopspiderCommodityidDownloaderMiddleware': None,
'AimShopSpider_CommodityID.middlewares.SeleniumFirefoxRenderAjaxDownloaderMiddleware':543,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'AimShopSpider_CommodityID.pipelines.AimshopspiderCommodityidPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


#这里的url链接是通过另外一个selenium+requests 方式编写的代码抓下来的，由于其中spm的参数不知道是何种加密方式即加密原始数据，而且不带这个参数调试后发现会少数据，
#所以这里才用了个笨方法，而且没有吧将两者合并在一起也是一个不足。


Database = {
    'IP':'xxxx',
    'USERNAME':'xxxx',
    'PASSWORD':'xxxx',
    'DB_NAME':'xxxxx',
}

account =b'xxxxxx'

# \u78B0\u8FD0\u6C141006
