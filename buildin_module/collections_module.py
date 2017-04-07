from collections import namedtuple, deque

# 创建namdtuple对象，这是一个自定义tuple对象
Td_vector = namedtuple('td', ['x', 'y', 'z', 'rad'])
p = Td_vector(23, 34, 12, 23.2)
print(p.x, p.y, p.z, p.rad)
# namdtuple对象是tuple的子类
print(isinstance(p, tuple))

# deque是为了高效实现插入和删除操作的双向列表，适合队列和栈
q = deque(['a', 'b', 'c'])
q.append('x')
q.append('t')
print(q.pop())
q.appendleft('y')
print(q.popleft())
print(q)

# defaultdict在key不存在时，返回一个默认值
from collections import defaultdict
# 默认值通过回调函数返回
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])

# OrderedDict
from collections import OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(d)
print(od)
# 利用OrderedDict实现一个FIFO的dict
class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if(len(self) - containsKey >= self._capacity):
            last = self.popitem(last = False)
            print('remove:', last)
        if(containsKey):
            del self[key]
            print('set:', (key, value))
        else:
            print('add', (key, value))
        OrderedDict.__setitem__(self, key, value)

# Counter计数器
from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)
# 输出Counter({'r': 2, 'g': 2, 'm': 2, 'i': 1, 'p': 1, 'o': 1, 'n': 1, 'a': 1})
