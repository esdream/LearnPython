from collections import Iterator
maplist = map(str, [1, 2, 3, 4, 5])
print(isinstance(maplist, Iterator))
def printname():
    print(next(maplist))
