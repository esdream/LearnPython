import itertools
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x<= 10, natuals)
print(list(ns))
# cs = itertools.cycle('ABCDEFG')
# for c in cs:
#     print(c)

# ns = itertools.repeat('A', 3)
# for n in ns:
#     print(n)

for c in itertools.chain('ABC', 'XYZ'):
    print(c)

for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
    print(key, list(group))
