# -*- coding: utf-8 -*-
import math
#1
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(-99))
#2
def quadratic(a, b, c):
    n = (b*b)- (4*a*c)
    if not isinstance(a,(float,int))  or not isinstance(b,(float,int))  or not isinstance(c,(float,int)) :
       raise TypeError('Bad Operand Type')
    if n < 0:
        print('此方程无解')
    elif a == 0:
            x1 = -c / b
            x2 = x1
    else:
            n = math.sqrt(n)
            x1 = (-b+n) / (2*a)
            x2 = (-b-n) / (2*a)
    return(x1,x2)
# 测试:
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')