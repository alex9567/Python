import re
#1
print(re.match(r'^\d{3}\-\d{3,8}$', '010-12345'))
print(re.match(r'^\d{3}\-\d{3,8}$', '010 12345'))
test = '用户输入的字符串'
if re.match(r'正则表达式', test):
    print('ok')
else:
    print('failed')
#2分割字符串
print('a b   c'.split(' '))
print(re.split(r'\s+', 'a b   c'))
print( re.split(r'[\s\,]+', 'a,b, c  d'))
print(re.split(r'[\s\,\;]+', 'a,b;; c  d'))
#3分割数组
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m)
print(m.group(0))
print(m.group(1))
print(m.group(2))
#4提取字符串
t = '19:05:30'
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
print(m.groups())
#贪婪匹配
print(re.match(r'^(\d+)(0*)$', '102300').groups())
print(re.match(r'^(\d+?)(0*)$', '102300').groups())
#练习1
import re

re_mail = re.compile(r'[a-z]+\.*[a-z]+\@[a-z]+\.com')

def is_valid_email(addr):
    if re.match(re_mail,addr):
        print(addr)
        return True
    return False

# 测试:
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')
#练习2
import re

re_name = re.compile(r'\<*([a-zA-Z\s]+)\>*[a-zA-Z\s]*\@[a-z]+\.[a-z]{3}')

def name_of_email(addr):
    m = re.match(re_name,addr)
    if m:
        print(m.group(1))
        return m.group(1)
    return False
# 测试:
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')

