# -*- coding: utf-8 -*-
#1
from functools import reduce
def normalize(name):
    return name[:1].upper()+name[1:].lower()
# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

#2
def prod(L):
    def mtply(elmt1,elmt2):
        return elmt1*elmt2
    return reduce(mtply,L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')
#3
from functools import reduce

def str2float(s):

    n=0
    for i in range(len(s)):
        if s[i]=='.':
            n=i
            break
    s1=s[:n]
    s2=s[:n:-1]
    digit={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    def str2int(s):
        return digit[s]
    def cmpt1(x,y):
        return x*10+y
    def cmpt2(x,y):
        return x/10+y
    return reduce(cmpt1,map(str2int,s1))+reduce(cmpt2,map(str2int,s2))/10

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
	
	
	