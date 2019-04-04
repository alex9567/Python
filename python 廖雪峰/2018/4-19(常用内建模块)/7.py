#itertools提供的几个“无限”迭代器：
import itertools
natuals = itertools.count(1)
#for n in natuals:
#    print(n)
#cycle()会把传入的一个序列无限重复下去：
cs = itertools.cycle('ABC') # 注意字符串也是序列的一种
#for c in cs:
#    print(c)
#repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数：
ns = itertools.repeat('A', 3)
for n in ns:
    print(n)
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)
print(list(ns))
#chain()可以把一组迭代对象串联起来，形成一个更大的迭代器：
for c in itertools.chain('ABC', 'XYZ'):
    print(c)
#groupby()把迭代器中相邻的重复元素挑出来放在一起：
for key, group in itertools.groupby('AAABBBCCAAA'):
	print(key, list(group))
#计算圆周率可以根据公式：

#利用Python提供的itertools模块，我们来计算这个序列的前N项和：
# -*- coding: utf-8 -*-
import itertools

def pi(N):
    ' 计算pi的值 '
# step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    natuals = itertools.count(1)
# step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    ns = itertools.takewhile(lambda x: x < N + 1, natuals)
    l = list(ns)
# step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    for i in range(len(l)):
        l[i] = 2 * l[i] - 1
        if (i % 2 == 1):
            l[i] = 0 - l[i]
        l[i] = 4 / l[i]
# step 4: 求和:
    return sum(l)
    return 3.14

# 测试:
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')