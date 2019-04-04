import time 
def func(n):  
    for i in range(0, n):  
        print('func: ', i)  
        yield i  
  
f = func(10) 
while True:  
    print(next(f))