#如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，
#在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    def print_score(std):
        print('%s: %s' % (std.__name, std.__score))
    def get_name(self):
    	return self.__name
    def set_name(self,name):
    	self.__name = name
    def get_score(self):
    	return self.__score
    def set_score(self,score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')
# -*- coding: utf-8 -*-
class Student(object):
    def __init__(self,name,gender):
        self.__name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender
        print('%s:%s' % (self.__name, self.__gender))

    def set_gender(self,gender):
        if gender == 'male':
            self.__gender = gender
        elif gender == 'female':
            self.__gender = gender
        else:
            raise ValueError('WRONG')
# 测试:
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')