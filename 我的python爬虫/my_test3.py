from urllib import request
from bs4 import BeautifulSoup
import re
import sys

if __name__ == "__main__":
	file = open('蛇皮.txt', 'w', encoding='utf-8')
	download_url = 'http://www.quanben2.com/quanben/261.html'
	head = {}
	head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
	download_req = request.Request(url = download_url, headers = head)
	download_response = request.urlopen(download_req)
	download_html = download_response.read().decode('gbk','ignore')
	soup_texts = BeautifulSoup(download_html, 'lxml')
	texts = soup_texts.find_all("ul")
	soup_text = BeautifulSoup(str(texts[1]), 'lxml')
	soup_text = soup_text.find_all("li");
	numbers = (len(soup_text) - 1)
	index = 1
    #遍历ul标签下所有子节点
	for child in soup_text:
		if child != '\n' and child.text != '查看书评':
			download_url = "http://www.quanben2.com/" + child.a.get('href')
			download_name = child.a.get('title')
			download_req = request.Request(url = download_url, headers = head)
			download_response = request.urlopen(download_req)
			download_html = download_response.read().decode('gbk','ignore')
			down_texts = BeautifulSoup(download_html, 'lxml')
			texts = down_texts.find_all(id = 'content',class_ = 'readcc')
			soup_text = BeautifulSoup(str(texts), 'lxml')
			file.write(download_name + '\n\n')
			file.write(soup_text.section.text)
			file.write('\n\n')
			#打印爬取进度
			sys.stdout.write("已下载:%.3f%%" % float(index/numbers*100) + '\r')
			sys.stdout.flush()
			index += 1
	file.close()
	#file.write(soup_text.section.text + '\n\n')
	#file.close()
	#print(soup_text.div.text.replace('\xa0',''))