import os
print(os.listdir('.'))
print([d for d in os.listdir('.')])

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str) is True]
print(L2)
