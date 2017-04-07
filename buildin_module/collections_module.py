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
