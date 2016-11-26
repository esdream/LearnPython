def is_odd(n):
    return n % 2 == 1

oddNum = list(filter(is_odd, [1, 2, 3, 4, 5, 6, 9, 10, 15]))
print(oddNum)

def not_empty(s):
    return s and s.strip()

func = filter(not_empty, ['A', '', 'B', None, 'C', '  '])
print(next(func))
print(next(func))
print(next(func))
