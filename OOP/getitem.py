class Fib(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a,b = b, a + b
        return a
print(list(range(100))[5:10])
