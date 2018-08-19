#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/6/26 17:15
# @Author   : z_jian
# @contact  : zjian1425@gmail.com
# @File     : Random_func.py

import random
import pandas as pd

def get_referer(com_id):
    return str('https://item.jd.com/{0}.html'.format(com_id))

def Random_WaitTime(flag):
    '''generate random waitting time'''
    if flag=='turnover':
        '''turnover page waitting'''
        t1 = random.uniform(5,10)
        print('now turnover page waitting time:{0}'.format(t1))
        return t1 #generate float

    elif flag=='jump':
        '''jump waitting'''
        t2 = random.uniform(5,10)
        print('now_jump_waitting:{0}'.format(t2))
        return t2 #generate float

    elif flag=='sleep':
        '''sleep waitting'''
        t3 = random.uniform(60,120)
        print('sleep waitiing:{0}'.format(t3))
        return t3 #generate float

    else:
        print('flag only input 0/1,now imput{0}'.format(flag))


def Random_Headers(com_id):
    '''switch ua'''
    UA_List = [
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
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
        'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;',
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)',
        'Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10'
    ]
    '''return dict'''
    headers = {
        'user-agent':random.choice(UA_List),
        'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'cache - control': 'max - age = 0',
        'accept - language': 'zh - CN, zh;q = 0.9',
        'accept_encoding':'gzip,deflate,br',
        'upgrade-insecure-requests':'1',
        'referer':get_referer(com_id)   #call get_referer
    }
    return headers

def Random_IpProxy():
    '''read ip_pool'''
    df = pd.read_csv('D:\JNBY_com_comments\proxiy_pool\ip_pool.csv')
    data = list(df['IP'])
    '''random return ip'''
    return {'https':random.choice(data)}



def Random_Cookies():
    '''cookies dict'''
    cookies_list =[
    {
        '__jdu':'1839807026',
        'PCSYCityID':'1213',
        'shshshfpa': '94c860c8-802f-d4fc-ac8e-504106ee99f4-1533006681',
        'shshshfpb': '00280ef1e94a43e539607b8a658b34935aaf8ef68c16c53515b5fd380a',
        'ipLoc-djd': '1-72-2799-0',
        'user-key': '3466e0ab-544a-4555-b990-cc558c0cbaa5',
        '_pst': 'jd_7dbcc0d507e50',
        'unick': 'jd_7dbcc0d507e50',
        'pin': 'jd_7dbcc0d507e50',
        '_tp': 'ClsOuI00UMDdsoohJ51%2FGEp2yZwlSd1yUciHE7DSatg%3D',
        'unpl': 'V2_ZzNtbUZVQ0J0AEFXKxpYDWIGRVVLXhEdIQBOV3IYWlZhUBJcclRCFXwUR11nGFwUZgsZXkpcQhNFCHZXchBYAWcCGllyBBNNIEwHDCRSBUE3XHxcFVUWF3RaTwEoSVoAYwtBDkZUFBYhW0IAKElVVTUFR21yVEMldQl2VHIbVAxmBRNeRWdzEkU4dlF7GVUMVwIiXHIVF0lwCUFUexoRBW4BGlRDUUIWcjhHZHg%3d',
        '__jdv': '122270672|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_531f0962a25944f988c9e992807b7b10|1533086955067',
        'TrackID': '1CaqsS9zplBT6DVArAA4aGhHisccU0_EGskLL_4EDvp0WdWJERZ1C76vMWPoA0tfYBXhPkwP1PicwqVjMhXuhWxnmKyAQQ7nlMo6QXOVYuJk',
        'pinId': 'hncu_uy-3DLFBjlFC_Qs7LV9-x-f3wj7',
        'shshshfp': 'e58a4c08f191312e7eb744da840063f1',
        'cn': '0',
        '__jda': '122270672.1839807026.1533006679.1533105517.1533174369.4',
        '__jdc': '122270672',
        '3AB9D23F7A4B3C9B': 'WGCIWKYGYK7GCZWGUSRX4NFCT4SHHS65GKNGVQMMRIEWESN4VPSANJJ37YDIZGSI5FMC4NKOZP6LSNWSFBIJFOF2EI'
    },
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
    return random.choice(cookies_list)