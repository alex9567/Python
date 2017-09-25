# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import requests
import os
import time
import re
if __name__ == '__main__':
	list_url = []
	#for num in range(1,3)
	url = 'http://desk.zol.com.cn/bizhi/7167_88668_2.html' #% num
	headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
	req = requests.get(url = url,headers = headers)
	req.encoding = 'gb2312'
	html = req.text
	bf = BeautifulSoup(html,'lxml')
	result = bf.find_all('ul',id='showImg')
	bf2 = BeautifulSoup(str(result),'lxml')
	result2 = bf2.find_all('a')
	print(result2[0].get('href'))
	print(len(result2))