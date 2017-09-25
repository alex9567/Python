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
	index2 = 0
	for num in range(10,13):
		url = 'http://desk.zol.com.cn/meinv/%d.html' % num
		headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
		req = requests.get(url = url,headers = headers)
		req.encoding = 'gb2312'
		html = req.text
		bf1 = BeautifulSoup(html,'lxml')
		#获得当页的所有图片合集url
		result1 = bf1.find_all('a',class_='pic')
		for num in range(0,15):
			#获得详细的图片地址
			resulturl = result1[num].get('href')
			resulturl2 = "http://desk.zol.com.cn"+resulturl
			req = requests.get(url = resulturl2,headers = headers)
			req.encoding = 'gb2312'
			html = req.text
			bf = BeautifulSoup(html,'lxml')
			result = bf.find_all('ul',id='showImg')
			bf2 = BeautifulSoup(str(result),'lxml')
			result2 = bf2.find_all('a')
			num1 = len(result2)-1
			for num in range(0,num1):
				list_url1.append("http://desk.zol.com.cn"+result2[num].get('href'))
			index2 +=1
			print("完成"+str(index2)+"个合集url获得")
	numbers = len(list_url1)
	index = 1
	print('一共有'+str(numbers)+"张图片")
	#获得1080P的具体图片地址，如果没有就跳过下载
	for url1 in list_url1:
		url = url1
		req = requests.get(url = url,headers = headers)
		req.encoding = 'gb2312'
		html = req.text
		bf2 = BeautifulSoup(html,'lxml')
		result2 = bf2.find_all('a',id='1920x1080')
		filename1 = bf2.find_all('a',id='titleName')[0].text
		filename2 = bf2.find_all('span',class_='current-num')[0].text
		filename = filename1+filename2+'.jpg'
		if len(result2)>0:
			#进行实际的下载
			url = 'http://desk.zol.com.cn/'+result2[0].get('href')
			req = requests.get(url = url,headers = headers)
			req.encoding = 'gb2312'
			html = req.text
			bf = BeautifulSoup(html,'lxml')
			result = bf.find_all('img')
			img_url = result[0].get('src')
			if 'images' not in os.listdir():
				os.makedirs('images')
			print("img_url:"+img_url)
			try:
				urlretrieve(url = img_url,filename = 'images/' + filename)
			except:
				print("发生异常，下载失败，跳过该图片")
			else: 
				print('下载：' + filename+"完成,"+"已下载:%.3f%%" % float(index/numbers*100))
			index +=1
		else:
			print('没有1080p,跳过下载')
			index +=1
	print('下载完成')
