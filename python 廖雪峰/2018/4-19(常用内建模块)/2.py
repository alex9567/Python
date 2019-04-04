from collections import namedtuple
from collections import deque
from collections import defaultdict
from collections import OrderedDict
#一个二维数组的代表
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x)
print(p.y)
print(isinstance(p, Point))
print(isinstance(p, tuple))
#用坐标半径表示一个园
Circle = namedtuple('Circle', ['x', 'y', 'r'])
#list数组读取快插入慢，用deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
q = deque(['a', 'b', 'c'])
q.append('x')
q.append('y')
print(q)
#appendleft()和popleft()头部和尾部添加。比较方便
#使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict：
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1']) # key1存在
print(dd['key2']) # key2不存在，返回默认值
#使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
#如果要保持Key的顺序，可以用OrderedDict：
d = dict([ ('a', 1),('b', 2), ('c', 3)])
print(d) # dict的Key是无序的
od = OrderedDict([ ('a', 1),('b', 2), ('c', 3)])
print(od)# OrderedDict的Key是有序的
#注意，OrderedDict的Key会按照插入的顺序排列，不是Key本身排序：
od = OrderedDict()
od['z'] = 1
od['y'] = 2
od['x'] = 3
print(list(od.keys())) # 按照插入的Key的顺序返回
#OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key：

from collections import OrderedDict

class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)
from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)