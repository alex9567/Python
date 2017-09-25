# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import requests
import os
import time
import re
if __name__ == '__main__':
	list_url1 = []
	list_url2 = []
	for num in range(1,2):
		url = 'http://desk.zol.com.cn/meinv/%d.html' % num
		headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
		req = requests.get(url = url,headers = headers)
		req.encoding = 'gb2312'
		html = req.text
		bf1 = BeautifulSoup(html,'lxml')
		result1 = bf1.find_all('a',class_='pic')
		bf2 = BeautifulSoup(str(result1[0]),'lxml')
		result2 =bf2.find_all("span")[0].text 
		result3 = re.findall("\d+",result2)
		for num in range(0,15):
			resulturl = result1[num].get('href')
			print(resulturl)
	#print(result[0].get('href'))
	#print(bf.find_all('a',id='titleName')[0].text)
	#print(bf.find_all('span',class_='current-num')[0].text)
	#print(bf2)