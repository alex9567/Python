print('one')
def foo(s):
    n = int(s)
    print('>>> n = %d' % n)
    return 10 / n

def main():
    foo('0')

#main()
print('two')
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

def main():
    foo('0')
#main()
import logging
logging.basicConfig(level=logging.INFO)#会输出错误信息
s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)
print('end')
#第4种方式是启动Python的调试器pdb，让程序以单步方式运行，可以随时查看运行状态。我们先准备好程序：