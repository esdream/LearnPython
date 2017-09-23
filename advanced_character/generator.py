def fib(max):
    n, a, b = 0, 0, 1
    while(n < max):
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

for x in fib(6):
    print(x)

u = fib(10)
print(next(u))
print(next(u))