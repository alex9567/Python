class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name: %s)' % self.name
    __repr__ = __str__
#打印出一堆<__main__.Student object at 0x109afb190>，不好看。
#怎么才能打印得好看呢？只需要定义好__str__()方法，返回一个好看的字符串就可以了：
print(Student('Michael'))
#但是细心的朋友会发现直接敲变量不用print，打印出来的实例还是不好看：
s = Student('Michael')
#解决办法是再定义一个__repr__()。但是通常__str__()和__repr__()代码都是一样的，
print(s)
#如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象
#然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值
for n in Fib():
    print(n)
#Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行，比如，取第5个元素：
#print(Fib()[5])
#要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：
class Fib(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a
f = Fib()
print(f[0])
#但是list有个神奇的切片方法：
print(list(range(100))[5:10])
#对于Fib却报错。原因是__getitem__()传入的参数可能是一个int，也可能是一个切片对象slice，所以要做判断：
class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int): # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L
#现在试试Fib的切片：
f = Fib()
print(f[0:5])
#但是没有对step参数作处理：
print(f[:10:2])
#也没有对负数作处理，所以，要正确实现一个__getitem__()还是有很多工作要做的。
class Student(object):

    def __init__(self):
        self.name = 'Michael'
#调用name属性，没问题，但是，调用不存在的score属性，就有问题了：
s = Student()
print(s.name)
#print(s.score)
#要避免这个错误，除了可以加上一个score属性外，Python还有另一个机制，那就是写一个__getattr__()方法，动态返回一个属性。修改如下：
class Student(object):

    def __init__(self):
        self.name = 'Michael'
    def __getattr__(self, attr):
        if attr=='score':
            return 99
s = Student()
print(s.name)
print(s.score)
#返回函数也是完全可以的：
class Student(object):

    def __getattr__(self, attr):
        if attr=='age':
            return lambda: 25
s = Student()
print(s.age())
#注意，只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找
#此外，注意到任意调用如s.abc都会返回None，这是因为我们定义的__getattr__默认返回就是None。要让class只响应特定的几个属性，我们就要按照约定，抛出AttributeError的错误：
print(s.abc)
class Student(object):

    def __getattr__(self, attr):
        if attr=='age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
s = Student()
#print(s.abc)
#如果要写SDK，给每个URL对应的API都写一个方法，那得累死，而且，API一旦改动，SDK也要改。
#利用完全动态的__getattr__，我们可以写出一个链式调用：
class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__
print(Chain().status.user.timeline.list)
#还有些REST API会把参数放到URL中，比如GitHub的API：
#GET /users/:user/repos
#print(Chain().users('michael').repos)
class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)
s = Student('Michael')
s()
print(callable(Student('test')))
print(callable(max))
print(callable([1, 2, 3]))
print(callable(None))
print(callable('str'))