print(type(123))
print(type(abs))
print(type(123)==type(456))
print(type(123)==int)
print(type('abc')==type('123'))
print(type('abc')==str)
print(type('abc')==type(123))
import types
def fn():
	pass
print(type(fn)==types.FunctionType)
print(type(abs)==types.BuiltinFunctionType)
print(type(lambda x: x)==types.LambdaType)
print(type((x for x in range(10)))==types.GeneratorType)
class Animal(object):
    pass
class Dog(Animal):
    pass
class Husky(Dog):
    pass
a = Animal()
d = Dog()
h = Husky()
print(isinstance(h, Husky))
print(isinstance(h, Dog))
print(isinstance(h, Animal))
print(isinstance(d, Dog) and isinstance(d, Animal))
print(isinstance(d, Husky))
print(isinstance('a', str))
print(isinstance(123, int))
print(isinstance(b'a', bytes))
print(isinstance([1, 2, 3], (list, tuple)))
print(isinstance((1, 2, 3), (list, tuple)))
print(dir('ABC'))
print(len('ABC'))
print( 'ABC'.__len__())
class MyDog(object):
	def __len__(self):
		return 100
dog = MyDog()
print(len(dog))
print( 'ABC'.lower())
class MyObject(object):
	def __init__(self):
		self.x = 9
	def power(self):
		return self.x * self.x
obj = MyObject()
print(hasattr(obj,'x'))
print(obj.x)
print(hasattr(obj, 'y'))# 有属性'x'吗？
print(setattr(obj, 'y', 19))# 有属性'y'吗？
print(hasattr(obj, 'y'))# 有属性'y'吗？
print(getattr(obj, 'y'))# 获取属性'y'
print(obj.y)
#如果去获得没有的属性，就会报错
#getattr(obj, 'z')
#可以传入一个default参数，如果属性不存在，就返回默认值
print(getattr(obj, 'z', 404))# 获取属性'z'，如果不存在，返回默认值404
print(hasattr(obj, 'power'))# 有属性'power'吗？
print(getattr(obj, 'power'))# 获取属性'power'
fn = getattr(obj, 'power')# 获取属性'power'并赋值到变量fn
print(fn)# fn指向obj.power
print(fn())#调用fn()与调用obj.power()是一样的
#通过内置的一系列函数，我们可以对任意一个Python对象进行剖析，拿到其内部的数据。
#要注意的是，只有在不知道对象信息的时候，我们才会去获取对象信息。如果可以直接写：
sum = obj.x + obj.y
#就不要写：
sum = getattr(obj, 'x') + getattr(obj, 'y')
#一个正确的用法的例子如下
def readImage(fp):
    if hasattr(fp, 'read'):
        return readData(fp)
    return None