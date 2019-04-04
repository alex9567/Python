#如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，
#在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def print_score(std):
        print('%s: %s' % (std.name, std.score))
    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'
bart = Student('Bart Simpson', 59)
print('名字:'+bart.name+',成绩：'+str(bart.score))
bart.print_score()
print(bart.get_grade())
lisa = Student('Lisa', 99)
bart = Student('Bart', 59)
print(lisa.name, lisa.get_grade())
print(bart.name, bart.get_grade())