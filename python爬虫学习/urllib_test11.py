# -*- coding: UTF-8 -*-
from urllib import request

if __name__ == "__main__":
    #访问网址
    url = 'http://www.whatismyip.com.tw/'
    #这是代理IP
    proxy = {'http':'61.174.61.15:808'}
    proxy_support = request.ProxyHandler(proxy)
    opener = request.build_opener(proxy_support)
    opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')]
    #安装OPener
    request.install_opener(opener)
    response = request.urlopen(url)
    html = response.read().decode('utf-8')
    print(html)