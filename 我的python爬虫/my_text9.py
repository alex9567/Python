from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import requests
import os
import time
if __name__ == '__main__':
	list_url = []
	#for num in range(1,3)
	url = 'http://desk.zol.com.cn//showpic/1920x1080_88668_28.html' #% num
	headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
	req = requests.get(url = url,headers = headers)
	req.encoding = 'gb2312'
	html = req.text
	bf = BeautifulSoup(html,'lxml')
	result = bf.find_all('img')
	print(result[0].get('src'))