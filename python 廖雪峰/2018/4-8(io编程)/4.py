import pickle
d = dict(name='Bob', age=20, score=88)
print(pickle.dumps(d))
f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()
f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close()
print(d)
import json

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob', 20, 88)
def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }
print(json.dumps(s, default=student2dict))
{"age": 20, "name": "Bob", "score": 88}
print(json.dumps(s, default=lambda obj: obj.__dict__))
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))
#习题
# -*- coding: utf-8 -*-

import json
obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=True)
print(s)
#中文需要指定为false