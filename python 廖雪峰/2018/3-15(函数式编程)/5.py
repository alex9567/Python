a = int('12345')
print(a)
a = int('12345', base=8)
print(a)
a = int('12345', 16)
print(a)
def int2(x, base=2):
    return int(x, base)
a = int2('1000000')
print(a)
a = int2('1010101')
print(a)
import functools
int2 = functools.partial(int, base=2)
a = int2('1000000')
print(a)
a = int2('1010101')
print(a)
max2 = functools.partial(max, 10)
args = (10, 5, 6, 7)
max(*args)
print(max)
