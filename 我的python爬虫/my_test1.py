from urllib import request
from bs4 import BeautifulSoup
import re
import sys

if __name__ == "__main__":
	file = open('乱.txt', 'w', encoding='utf-8')
	download_url = 'http://www.quanben2.com/txt_read/13023part1.html'
	head = {}
	head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
	download_req = request.Request(url = download_url, headers = head)
	download_response = request.urlopen(download_req)
	download_html = download_response.read().decode('gbk','ignore')
	soup_texts = BeautifulSoup(download_html, 'lxml')
	texts = soup_texts.find_all(id = 'content',class_ = 'readcc')
	soup_text = BeautifulSoup(str(texts), 'lxml')
	print(soup_text.section.text)
	#file.write(soup_text.section.text + '\n\n')
	#file.close()
	#print(soup_text.div.text.replace('\xa0',''))