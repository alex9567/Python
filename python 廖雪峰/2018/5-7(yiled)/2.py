import time  
def func(n):  
    for i in range(0, n):  
        arg = yield i  
        print('func:', arg)  
  
f = func(10)  
while True:  
    print('main1:', next(f))
    print('main2:',f.send(100))