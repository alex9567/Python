# -*- coding: utf-8 -*-
#排序数字
sorted([36, 5, -12, 9, -21])
#排序数字绝对值
sorted([36, 5, -12, 9, -21], key=abs)
#排序字符串
sorted(['bob', 'about', 'Zoo', 'Credit'])
#排序字符串，忽略大小写排序
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
#请用sorted()对上述列表分别按名字排序：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
     return t[0]
L2 = sorted(L, key=by_name)
print(L2)
def by_score(t):
     return t[1]
L2 = sorted(L, key=by_score)
print(L2)