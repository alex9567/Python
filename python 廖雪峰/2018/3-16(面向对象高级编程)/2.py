#在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，但是，没办法检查参数，导致可以把成绩随便改：
#这显然不合逻辑。为了限制score的范围，
#可以通过一个set_score()方法来设置成绩，再通过一个get_score()来获取成绩，
#这样，在set_score()方法里，就可以检查参数：
class Student(object):

    def get_score(self):
         return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
s = Student()
s.set_score(60) # ok!
print(s.get_score())
#s.set_score(9999)#会报错
#但是上面的方法又不是很好
#对于类的方法，装饰器一样起作用。Python内置的@property装饰器就是负责把一个方法变成属性调用的：
class Student(object):
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
s = Student()
s.score = 60 # OK，实际转化为s.set_score(60)
print(s.score)# OK，实际转化为s.get_score()
#还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：
class Student(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth
s = Student()
s.birth = 60
print(s.age)
#请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：
# -*- coding: utf-8 -*-
class Screen(object):
    @property
    def width(self):
        return self._width
    @property
    def height (self):
        return self._height	
    @width.setter
    def width(self, value):
        self._width = value
    @height.setter
    def height(self, value):
        self._height = value
    @property
    def resolution(self):
        return self._width * self._height
# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')