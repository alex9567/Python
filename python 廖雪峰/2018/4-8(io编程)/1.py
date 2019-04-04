f = open('C:/Users/admin/Desktop/test.txt', 'r')
f.read()
print("one:")
try:
    f = open('C:/Users/admin/Desktop/test.txt', 'r')
    print(f.read())
finally:
    if f:
        f.close()
print("two:")
with open('C:/Users/admin/Desktop/test.txt', 'r') as f:
    print(f.read())
print("three:")
f = open('C:/Users/admin/Desktop/test.txt', 'r')
for line in f.readlines():
    print(line.strip()) # 把末尾的'\n'删掉
print("four:")
f = open('C:/Users/admin/Desktop/test.txt', 'rb')
f.read()
print("five:")
f = open('C:/Users/admin/Desktop/test.txt', 'w')
f.write('Hello, world!')
f.close()
print("sex:")
with open('C:/Users/admin/Desktop/test.txt', 'w') as f:
    f.write('Hello, world!')
#请将本地一个文本文件读为一个str并打印出来：
print("练习：")
# -*- coding: utf-8 -*-
fpath = r'C:/Users/admin/Desktop/test.txt'
with open(fpath, 'r') as f:
    s = f.read()
    print(s)
