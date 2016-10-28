from math import sqrt
def cal(x, *fs):
    s = [f(x) for f in fs]
    return s

print(cal(2, sqrt, abs))
