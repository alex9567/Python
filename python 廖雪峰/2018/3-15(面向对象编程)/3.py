#简单继承
class Animal(object):
    def run(self):
        print('Animal is running...')
class Dog(Animal):
    pass
class Cat(Animal):
    pass
dog = Dog()
dog.run()
cat = Cat()
cat.run()
#修改后的继承
class Dog(Animal):
    def run(self):
        print('Dog is running...')
    def eat(self):
        print('Eating meat...')
class Cat(Animal):
    def run(self):
        print('Cat is running...')
dog = Dog()
dog.run()
cat = Cat()
cat.run()
#Dog是从Animal继承下来的，当我们创建了一个Dog的实例c时，我们认为c的数据类型是Dog没错，但c同时也是Animal也没错，Dog本来就是Animal的一种！
a = list() # a是list类型
b = Animal() # b是Animal类型
c = Dog() # c是Dog类型
print(isinstance(a, list))
print(isinstance(b, Animal))
print(isinstance(c, Dog))
print(isinstance(c, Animal))
#Dog可以看成Animal，但Animal不可以看成Dog。
b = Animal()
print(isinstance(b, Dog))
def run_twice(animal):
    animal.run()
    animal.run()
run_twice(Animal())
run_twice(Dog())
run_twice(Cat())
#如果我们再定义一个Tortoise类型，也从Animal派生：
class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')
run_twice(Tortoise())
#这就是多态
class Timer(object):
    def run(self):
        print('Start...')
run_twice(Timer())
