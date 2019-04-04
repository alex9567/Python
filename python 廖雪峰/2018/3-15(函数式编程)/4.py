#函数
def now():
    print('2015-3-25')
f = now
print(f())
#函数嵌套
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
@log
def now():
	print('2015-3-25')
f = now
print(f())
#函数嵌套赋值
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
@log('execute')
def now():
    print('2015-3-25')
f = now
print(f())
#请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
# -*- coding: utf-8 -*-
import time, functools
def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        t = time.time()
        fn(*args,**kw)
        t2 = time.time()
        print('%s executed in %0.3f ms' % (fn.__name__, t2 -t))
        return fn(*args, **kw)
    return wrapper
# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')