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
DOWNLOAD_DELAY = 3
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
AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


#这里的url链接是通过另外一个selenium+requests 方式编写的代码抓下来的，由于其中spm的参数不知道是何种加密方式即加密原始数据，而且不带这个参数调试后发现会少数据，
#所以这里才用了个笨方法，而且没有吧将两者合并在一起也是一个不足。

veromoda = {
'https://veromoda.tmall.com/category.htm?spm=a1z10.3-b-s.w4011-14529808362.118.e0163592OsYtbU&search=y&scene=taobao_shop&pageNo=2#anchor',
'https://veromoda.tmall.com/category.htm?spm=a1z10.3-b-s.w4011-14529808362.119.963c3592dWJ8sy&search=y&scene=taobao_shop&pageNo=3#anchor',
'https://veromoda.tmall.com/category.htm?spm=a1z10.3-b-s.w4011-14529808362.119.55e13592q8cLsy&search=y&scene=taobao_shop&pageNo=4#anchor',
'https://veromoda.tmall.com/category.htm?spm=a1z10.3-b-s.w4011-14529808362.107.4b113592cAFcog&search=y&scene=taobao_shop&pageNo=5#anchor',
'https://veromoda.tmall.com/category.htm?spm=a1z10.3-b-s.w4011-14529808362.119.1fd53592OimYAB&search=y&scene=taobao_shop&pageNo=6#anchor',
'https://veromoda.tmall.com/category.htm?spm=a1z10.3-b-s.w4011-14529808362.119.25b83592NIHaQ2&search=y&scene=taobao_shop&pageNo=7#anchor',
'https://veromoda.tmall.com/category.htm?spm=a1z10.3-b-s.w4011-14529808362.119.721235927iRlML&search=y&scene=taobao_shop&pageNo=8#anchor',
'https://veromoda.tmall.com/category.htm?spm=a1z10.3-b-s.w4011-14529808362.119.2db83592xFG58i&search=y&scene=taobao_shop&pageNo=9#anchor',
'https://veromoda.tmall.com/category.htm?spm=a1z10.3-b-s.w4011-14529808362.119.69e23592moZlZZ&search=y&scene=taobao_shop&pageNo=10#anchor',
'https://veromoda.tmall.com/category.htm?spm=a1z10.3-b-s.w4011-14529808362.119.6f703592FuKT77&search=y&scene=taobao_shop&pageNo=11#anchor',
'https://veromoda.tmall.com/category.htm?spm=a1z10.3-b-s.w4011-14529808362.107.5a083592mEejD4&search=y&scene=taobao_shop&pageNo=12#anchor',
'https://veromoda.tmall.com/category.htm?spm=a1z10.3-b-s.w4011-14529808362.119.10b43592DZp63I&search=y&scene=taobao_shop&pageNo=13#anchor',
'https://veromoda.tmall.com/category.htm?spm=a1z10.3-b-s.w4011-14529808362.107.45e33592datIpL&search=y&scene=taobao_shop&pageNo=14#anchor',
'https://veromoda.tmall.com/category.htm?spm=a1z10.3-b-s.w4011-14529808362.107.19a53592mDp9MR&search=y&scene=taobao_shop&pageNo=15#anchor',
'https://veromoda.tmall.com/category.htm?spm=a1z10.3-b-s.w4011-14529808362.119.5b6335927Bgtbd&search=y&scene=taobao_shop&pageNo=16#anchor',
'https://veromoda.tmall.com/category.htm?spm=a1z10.3-b-s.w4011-14529808362.119.6d653592L5Uqk0&search=y&scene=taobao_shop&pageNo=17#anchor',
'https://veromoda.tmall.com/category.htm?spm=a1z10.3-b-s.w4011-14529808362.107.65eb3592Whntn4&search=y&scene=taobao_shop&pageNo=18#anchor',
'https://veromoda.tmall.com/category.htm?spm=a1z10.3-b-s.w4011-14529808362.119.7bcc35920mSaVo&search=y&scene=taobao_shop&pageNo=19#anchor',
'https://veromoda.tmall.com/category.htm?spm=a1z10.3-b-s.w4011-14529808362.119.57583592hn3yhV&search=y&scene=taobao_shop&pageNo=20#anchor',
'https://veromoda.tmall.com/category.htm?spm=a1z10.3-b-s.w4011-14529808362.119.7f793592c1LcAc&search=y&scene=taobao_shop&pageNo=21#anchor',
'https://veromoda.tmall.com/category.htm?spm=a1z10.3-b-s.w4011-14529808362.107.5f913592sKwahh&search=y&scene=taobao_shop&pageNo=22#anchor',
'https://veromoda.tmall.com/category.htm?spm=a1z10.3-b-s.w4011-14529808362.119.77363592FOM4FR&search=y&scene=taobao_shop&pageNo=23#anchor',
'https://veromoda.tmall.com/category.htm?spm=a1z10.3-b-s.w4011-14529808362.107.86d63592x69Ylt&search=y&scene=taobao_shop&pageNo=24#anchor',
'https://veromoda.tmall.com/category.htm?spm=a1z10.3-b-s.w4011-14529808362.107.451d3592ZBuRyx&search=y&scene=taobao_shop&pageNo=25#anchor',
'https://veromoda.tmall.com/category.htm?spm=a1z10.3-b-s.w4011-14529808362.119.5e7d3592UoQ222&search=y&scene=taobao_shop&pageNo=26#anchor',
'https://veromoda.tmall.com/category.htm?spm=a1z10.3-b-s.w4011-14529808362.107.5e9d3592sjmDtu&search=y&scene=taobao_shop&pageNo=27#anchor',
'https://veromoda.tmall.com/category.htm?spm=a1z10.3-b-s.w4011-14529808362.107.95bf35926GCix3&search=y&scene=taobao_shop&pageNo=28#anchor',
'https://veromoda.tmall.com/category.htm?spm=a1z10.3-b-s.w4011-14529808362.119.4e0f3592cWyHMf&search=y&scene=taobao_shop&pageNo=29#anchor',
'https://veromoda.tmall.com/category.htm?spm=a1z10.3-b-s.w4011-14529808362.119.702a3592FheMPb&search=y&scene=taobao_shop&pageNo=30#anchor',
'https://veromoda.tmall.com/category.htm?spm=a1z10.3-b-s.w4011-14529808362.119.4e873592z8HDYZ&search=y&scene=taobao_shop&pageNo=31#anchor',
'https://veromoda.tmall.com/category.htm?spm=a1z10.3-b-s.w4011-14529808362.119.3ef13592I1pJHb&search=y&scene=taobao_shop&pageNo=32#anchor',
'https://veromoda.tmall.com/category.htm?spm=a1z10.3-b-s.w4011-14529808362.119.69a935926e2leh&search=y&scene=taobao_shop&pageNo=33#anchor',
'https://veromoda.tmall.com/category.htm?spm=a1z10.3-b-s.w4011-14529808362.107.788b35920QOKBA&search=y&scene=taobao_shop&pageNo=34#anchor',
'https://veromoda.tmall.com/category.htm?spm=a1z10.3-b-s.w4011-14529808362.107.679a35926neMud&search=y&scene=taobao_shop&pageNo=35#anchor',
'https://veromoda.tmall.com/category.htm?spm=a1z10.3-b-s.w4011-14529808362.107.71983592xv1Peh&search=y&scene=taobao_shop&pageNo=36#anchor',
'https://veromoda.tmall.com/category.htm?spm=a1z10.3-b-s.w4011-14529808362.107.6fd23592HGR76C&search=y&scene=taobao_shop&pageNo=37#anchor',
'https://veromoda.tmall.com/category.htm?spm=a1z10.3-b-s.w4011-14529808362.165.43de3592hkFwwq&search=y&scene=taobao_shop&pageNo=38#anchor',
'https://veromoda.tmall.com/category.htm?spm=a1z10.3-b-s.w4011-14529808362.107.2c893592JF9aDU&search=y&scene=taobao_shop&pageNo=39#anchor',
'https://veromoda.tmall.com/category.htm?spm=a1z10.3-b-s.w4011-14529808362.119.1c5c3592Dxd70g&search=y&scene=taobao_shop&pageNo=40#anchor',
'https://veromoda.tmall.com/category.htm?spm=a1z10.3-b-s.w4011-14529808362.119.76703592gp3lPs&search=y&scene=taobao_shop&pageNo=41#anchor',
'https://veromoda.tmall.com/category.htm?spm=a1z10.3-b-s.w4011-14529808362.119.355035928mpL0E&search=y&scene=taobao_shop&pageNo=42#anchor',
'https://veromoda.tmall.com/category.htm?spm=a1z10.3-b-s.w4011-14529808362.119.3f813592wen9qC&search=y&scene=taobao_shop&pageNo=43#anchor',
'https://veromoda.tmall.com/category.htm?spm=a1z10.3-b-s.w4011-14529808362.119.7dcf3592iaFsyA&search=y&scene=taobao_shop&pageNo=44#anchor',
'https://veromoda.tmall.com/category.htm?spm=a1z10.3-b-s.w4011-14529808362.119.498e3592ozAdDf&search=y&scene=taobao_shop&pageNo=45#anchor',
'https://veromoda.tmall.com/category.htm?spm=a1z10.3-b-s.w4011-14529808362.119.37833592kymfqK&search=y&scene=taobao_shop&pageNo=46#anchor',
'https://veromoda.tmall.com/category.htm?spm=a1z10.3-b-s.w4011-14529808362.107.59af3592rIGlT2&search=y&scene=taobao_shop&pageNo=47#anchor',
'https://veromoda.tmall.com/category.htm?spm=a1z10.3-b-s.w4011-14529808362.119.66913592sQIvSt&search=y&scene=taobao_shop&pageNo=48#anchor',
'https://veromoda.tmall.com/category.htm?spm=a1z10.3-b-s.w4011-14529808362.119.435035926V5PZL&search=y&scene=taobao_shop&pageNo=49#anchor',
'https://veromoda.tmall.com/category.htm?spm=a1z10.3-b-s.w4011-14529808362.119.30c53592wSI5aK&search=y&scene=taobao_shop&pageNo=50#anchor',
'https://veromoda.tmall.com/category.htm?spm=a1z10.3-b-s.w4011-14529808362.119.3c733592yix2xg&search=y&scene=taobao_shop&pageNo=51#anchor',
'https://veromoda.tmall.com/category.htm?spm=a1z10.3-b-s.w4011-14529808362.119.57763592ZqIoIc&search=y&scene=taobao_shop&pageNo=52#anchor',
'https://veromoda.tmall.com/category.htm?spm=a1z10.3-b-s.w4011-14529808362.119.5e103592VNxkf7&search=y&scene=taobao_shop&pageNo=53#anchor',
'https://veromoda.tmall.com/category.htm?spm=a1z10.3-b-s.w4011-14529808362.119.606835920bkQkf&search=y&scene=taobao_shop&pageNo=54#anchor',
'https://veromoda.tmall.com/category.htm?spm=a1z10.3-b-s.w4011-14529808362.107.62963592ttDswC&search=y&scene=taobao_shop&pageNo=55#anchor',

}

Database = {
    'IP':'183.129.168.211',
    'USERNAME':'hexi',
    'PASSWORD':'hexi123',
    'DB_NAME':'db_ecommerce',
}

account ='g1200dragon'

