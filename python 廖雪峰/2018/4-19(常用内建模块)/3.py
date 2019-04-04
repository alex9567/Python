import base64
#Python内置的base64可以直接进行base64的编解码：
print(base64.b64encode(b'binary\x00string'))
print(base64.b64decode(b'YmluYXJ5AHN0cmluZw=='))
#由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_：
print(base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64decode('abcd--__'))
#由于=字符也可能出现在Base64编码中，但=用在URL、Cookie里面会造成歧义，所以，很多Base64编码后会把=去掉：
# 标准Base64:
#'abcd' -> 'YWJjZA=='
encodestr = base64.b64encode(b'abcr34r344r')
print(encodestr)
#去掉b，转码
print(str(encodestr,'utf-8'))
# 自动去掉=:
#'abcd' -> 'YWJjZA'
# -*- coding: utf-8 -*-

def safe_base64_decode(s):
    while len(s) % 4 != 0:
        s = s + b'='
    return base64.b64decode(s)
# 测试:
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')