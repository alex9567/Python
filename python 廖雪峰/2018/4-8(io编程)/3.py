import os
print("one:")
print(os.name)
#os.uname()#windows不提供
print(os.environ)
print(os.environ.get('PATH'))
print("two:")
print(os.path.abspath('.'))
print(os.path.join('G:/学习记录/python/python 廖雪峰/4-8(io编程)', 'testdir'))
os.mkdir('G:/学习记录/python/python 廖雪峰/4-8(io编程)/testdir')#创建目录
os.rmdir('G:/学习记录/python/python 廖雪峰/4-8(io编程)/testdir')#删除目录
print("three:")
print(os.path.split('C:/Users/admin/Desktop/test.txt'))
print(os.path.splitext('C:/Users/admin/Desktop/test.txt'))
print("four:")
print([x for x in os.listdir('.') if os.path.isdir(x)])
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])