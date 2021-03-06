# -*- coding: utf-8 -*-

# Scrapy settings for jd_comments project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'jd_comments'

SPIDER_MODULES = ['jd_comments.spiders']
NEWSPIDER_MODULE = 'jd_comments.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'jd_comments (+http://www.yourdomain.com)'

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
# COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'jd_comments.middlewares.JdCommentsSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'jd_comments.middlewares.JdCommentsDownloaderMiddleware': 443,
    # 'jd_comments.middlewares.JdNewDownloaderMiddleware':443,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'jd_comments.pipelines.JdCommentsPipeline': 300,
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
AUTOTHROTTLE_DEBUG = True

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

Database = {
    'IP':'',
    'USERNAME':'',
    'PASSWORD':'',
    'DB_NAME':'',
}


#已失效
CookiesList = [
    {
        '__jda': '122270672.15293061551681071550732.1529306155.1529306155.1533190868.1',
        'unpl': 'V2_ZzNtbRdSFxYiDhMBfR9VBWIDEQgSU0JCIFtBAS5MVVc0ABtfclRCFXwUR11nGF8UZwYZXkFcRh1FCEdkex5fDGQzFFRHUUQRdAt2ZHgZbA1XAxZeSlVCEnUMQlR8EFwEYQMWWUNRQRZFOEFkS83Jrr%2bIhQ8DFZql0N7s%2bkseWQJhChtYRmdCJXQ4DTp6VFwBZAsQXEVXRxF1D09Ueh9cAWMCFF9BZ0Ildg%3d%3d',
        '__jdb': '122270672.7.15293061551681071550732|1.1533190868',
        '__jdc': '122270672',
        '__jdv': '122270672|c.duomai.com|t_16282_78476502|tuiguang|d4e2f7dd7781412da50fdb6ddd8cb283|1533190867693',
        '__jdu': '15293061551681071550732',
        'PCSYCityID': '1211',
        'shshshfp': '91f056b60cb2841479301bba8b1c3275',
        'shshshfpa': '35fac8e3-1069-056e-3a3d-ee4807e11d0c-1533190871',
        'shshshsID': '103801622b6241cdbcdd46ff6debbf66_6_1533190923131',
        'shshshfpb': '2d07e4e77085f489bbd7e24a5cd1f67bb5720d2e160a70383fb62a33f0',
        '3AB9D23F7A4B3C9B': 'FJONM4D2EEM2OGP4ATCLORLMA6VUJEP74OGFERPCC5ZLFV3Y5OR4DL4OOPH2DV5VSB4JKLXDJKDQIOH66WSVBPOFJQ'
    },
    {
        'user-key': '1d638b67-8396-4621-a52a-ea68a0e3f864',
        'cn': '0',
        'PCSYCityID': '1212',
        'ipLoc-djd': '1-72-2799-0',
        'shshshfpa': 'bab66853-7278-6508-abaf-23c83bed10f2-1532588371',
        'unpl': 'V2_ZzNtbRcFE0VwCRZTfhBdVWIEEV0SVUodcglCUSkRCVJiAxNcclRCFXwUR11nGF8UZwYZX0BcRx1FCHZXchBYAWcCGllyDhNLN1YCFSNGF1wjU00zQwdKE3FdQVQpHQtRYgVHVBEFRhxyDk5UeRpUB2RWEV9yZ0AVRQhHZHsaWwRgChRYQF9zJXI4dmR%2bGV4DbwciXHJWc1chVEZQfhteDCoDEVpDUEoTcApOZHopXw%3d%3d',
        '__jda': '122270672.1260687439.1510470771.1532588145.1533191639.3',
        '__jdb': '122270672.1.1260687439|3.1533191639',
        '__jdc': '122270672',
        '__jdv': '122270672|haosou-pinzhuan|t_288551095_haosoupinzhuan|cpc|0a875d61c5fe47d8bc48679132932d23_0_dcaa40a6480a4621a3896054c9df4100|1533191638670',
        'shshshfp': 'c01dc06a7e62f4a2d67abe1f611a7e28',
        'shshshsID': '6ae525ebe07fd1287a9cdf267d1708ab_1_1533191640567',
        'shshshfpb': '0cd733616615ca25b49b6d78c38b04d2d854f4d5ed00d54ea5b5970711',
        '__jdu': '1260687439'
    },
    {
        '__jda':'122270672.732814383.1533191808.1533191808.1533191809.1',
        '__jdu':'732814383',
        'PCSYCityID':'1214',
        'shshshfpa':'c47dd2a1-26b4-7d19-7123-1fcf9bcc6a0b-1533191810',
        'shshshfpb':'10a3a6c2033c74c10b4c5abbc6d7902332a4552bec8fbca275b62a6bc7',
        'mt_xid':'V2_52007VwUQUVRYV1gWSylaAm5XEgJaWk4OGU0bQABuUBZODQhTDQNMEVQENwNGUl8LUw4vShhcDHsCG05cW0NaGkIbWg5jCiJSbVhiWR1LHFsDbgYRYl9cU18%3D',
        'user-key':'67ede85d-2427-470b-b8e7-909d64edf0f4',
        'cn':'0',
        'unpl':'V2_ZzNtbUpeQ0Z8AEBdeEsPDWIHFg1KVUMddQFOVHkaCVVhVhcJclRCFXwUR11nGF8UZwYZWEJcRhZFCEdkexhdBGcHGllBUnMldDhFVEsRbANlABtdR1VKF0U4QWRLGVkAbwEWX0ZSXxZwD0RceClaBGcCEl1BX0EldDhAVXIRXAdmChNtCTlCWHMKRV17HF4MZTMTbUE%3d',
        '__jdc':'122270672',
        '__jdb':'122270672.6.732814383|1.1533191809',
        '__jdv':'122270672|www.jiegeng.com|t_1000159524_|tuiguang|981b89782cb9455a9319189132da7d4e|1533192048980',
        'shshshfp':'60e622a9d859487e17bc6bd7dbabece8',
        'shshshsID':'6d413c996c865ad75ada52eae4cc260d_6_1533192049276'
    }
]

UA_list = [
        'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52',
        'Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)',
        'Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
        'Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)',
        'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)',
        'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)',
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)',
        'Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6',
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1',
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0',
        'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36',
        'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)',
        'Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+',
        'Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999',
        'MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
        'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
        'Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
        'Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
        'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;',
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)',
        'Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+',
        'Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13',
        'Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10',
        'NOKIA5700/ UCWEB7.0.2.37/28/999'
    ]

