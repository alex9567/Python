# -*- coding: utf-8 -*-
#删掉偶数，只保留奇数
def is_odd(n):
    return n % 2 == 1
name = [1, 2, 4, 5, 6, 9, 10, 15]
b = list(filter(is_odd, name))
for a in b:
	print(a)
#把一个序列中的空字符串删掉
def not_empty(s):
	return s and s.strip()
c = list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))
for a in c:
	print(a)
#注意这是一个生成器，并且是一个无限序列。
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n
#筛选函数
def _not_divisible(n):
    return lambda x: x % n > 0
#最后，定义一个生成器，不断返回下一个素数：
def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列
# 打印1000以内的素数:
for n in primes():
    if n < 1000:
        print(n)
    else:
        break

#练习，回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：
def is_palindrome(n):
    return int(str(n)[::-1])==n
# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')