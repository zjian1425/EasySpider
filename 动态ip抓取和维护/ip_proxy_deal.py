import  pymysql
import random
import requests
import telnetlib

class MySql(object):

	def  __init__(self):
		self.conn = pymysql.connect('xxxxxx','xxx','xxxx','xxxx',charset='utf8')
		self.cursor = self.conn.cursor()

	def __del__(self):
		self.conn.commit()
		self.cursor.close()
		self.conn.close()

	def execute(self,query):
		try:
			self.cursor.execute(query)
			print('execute_successed!!!')
		except:
			print('execute_failed!!!')

	def GetIPS(self,query):
		self.execute(query)
		result = self.cursor.fetchall()
		return result

	def Rondom_IP(self,query):
		list = []
		ver_list=[]
		tuple = self.GetIPS(query)
		for i in range(len(tuple)):
			list.append(tuple[i][0])
			# tuple[i] = tuple[i].strip(',')
		for i in list:
			usable_ip = self.Verity_Ip(i)
			if usable_ip:
				ver_list.append(usable_ip)
		return ver_list

	def Random_UA(self):
		USER_AGENTS = [
			"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
			"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
			"Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
			"Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
			"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
			"Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
			"Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
			"Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
			"Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
			"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
			"Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
			"Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
			"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
			"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
			"Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52", ]
		return random.choice(USER_AGENTS)

	def  Verity_Ip(self,IP):
		# proxies= {
		# 	'https':IP
		# }
		# U_A =self.Random_UA()
		# headers ={
		# 	'headers':U_A
		# }
		hd, port =IP.split(':')
		try:
			telnetlib.Telnet(hd,port=port,timeout=20)
			# res = requests.get('https://www.baidu.com/',proxies=proxies,headers=headers,timeout = 5)
			# if res.status_code == 200:
			print(IP+' vertify success')
			return IP
			# else:
			# 	res.raise_for_status()
			# 	return None
		except Exception as e:
			print("验证代理ip"+IP+"时发生如下错误:")
			print(e)
			del_query = '''delete from IP_POOL where ip=\'{0}\''''.format(IP)
			self.execute(del_query)
			return None


def main():
	query_sql = '''SELECT ip FROM IP_POOL  '''
	getIP =  MySql()
	ip_pool=getIP.Rondom_IP(query_sql)
	return ip_pool

if __name__ == '__main__':
	list=main()
	print(list)
	print('当前代理ip有效率:%f',(len(list)/240))