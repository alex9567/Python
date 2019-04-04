class Student(object):
    def __init__(self, name):
        self.name = name
s = Student('Bob')
print(s.name)
s.score = 90
print(s.score)
s.name = 'aaa'
print(s.name)
class Student(object):
    name = 'Student'
s = Student()# 创建实例s
print(s.name)# 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
print(Student.name)# 打印类的name属性
s.name = 'Michael'# 给实例绑定name属性
print(s.name)# 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
print(Student.name)# 但是类属性并未消失，用Student.name仍然可以访问
del s.name# 如果删除实例的name属性
print(s.name)# 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了
# -*- coding: utf-8 -*-
#为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加：
class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count = Student.count + 1
# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')
