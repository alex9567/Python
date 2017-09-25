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
		for num in range(0,15):
			resulturl = result1[num].get('href')
			print("主要地址："+resulturl)
			resulturl2 = "http://desk.zol.com.cn"+resulturl
			url = resulturl2
			headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
			req = requests.get(url = url,headers = headers)
			req.encoding = 'gb2312'
			html = req.text
			bf = BeautifulSoup(html,'lxml')
			result = bf.find_all('ul',id='showImg')
			bf2 = BeautifulSoup(str(result),'lxml')
			result2 = bf2.find_all('a')
			num1 = len(result2)-1
			for num in range(0,num1):
				print("http://desk.zol.com.cn"+result2[num].get('href'))