# -*- coding:UTF-8 -*-
from selenium import webdriver

if __name__ == '__main__':
    url = 'http://pythonscraping.com/pages/itsatrap.html'
    driver = webdriver.PhantomJS(executable_path='E:/phantomjs-2.1.1-windows/bin/phantomjs.exe')
    driver.get(url)
    links = driver.find_elements_by_tag_name('a')
    for link in links:
        if not link.is_displayed():
            print('连接:' + link.get_attribute('href') + ',是一个蜜罐圈套.')

    fields = driver.find_elements_by_tag_name('input')
    for field in fields:
        if not field.is_displayed():
            print('不要改变' + field.get_attribute('name') + '的值.')