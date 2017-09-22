from urllib import request
from bs4 import BeautifulSoup
import re
import sys

if __name__ == "__main__":
	file = open('乱.txt', 'w', encoding='utf-8')
	download_url = 'http://www.quanben2.com/quanben/13023.html'
	head = {}
	head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
	download_req = request.Request(url = download_url, headers = head)
	download_response = request.urlopen(download_req)
	download_html = download_response.read().decode('gbk','ignore')
	soup_texts = BeautifulSoup(download_html, 'lxml')
	texts = soup_texts.find_all("ul")
	soup_text = BeautifulSoup(str(texts[1]), 'lxml')
	soup_text = soup_text.find_all("li");
    #遍历ul标签下所有子节点
	for child in soup_text:
		if child != '\n' and child.text != '查看书评':
			download_url = "http://www.quanben2.com/" + child.a.get('href')
			download_name = child.a.get('title')
			print(download_name + " : " + download_url)
	#file.write(soup_text.section.text + '\n\n')
	#file.close()
	#print(soup_text.div.text.replace('\xa0',''))