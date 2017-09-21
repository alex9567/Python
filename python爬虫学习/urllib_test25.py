# -*- coding:UTF-8 -*-
from selenium import webdriver

if __name__ == '__main__':
    url = 'http://pythonscraping.com'
    driver = webdriver.PhantomJS(executable_path='E:/phantomjs-2.1.1-windows/bin/phantomjs.exe')
    driver.get(url)
    driver.implicitly_wait(1)
    print(driver.get_cookies())
