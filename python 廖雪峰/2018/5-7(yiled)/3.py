import time  
def func(n):  
    for i in range(0, n):
        arg = yield i
        print('func:', arg)
  
f = func(10)  
print('main1:', f.send(None))
while True:  
    print('main2:', f.send(100))