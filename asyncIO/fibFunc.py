import random
import time

def stupidFib(n):
    a = 0
    b = 1
    for i in range(n):
        sleepCnt = yield b
        print('let me think {0} secs'.format(sleepCnt))
        time.sleep(sleepCnt)
        a, b = b, a + b
print('-' * 10 + 'test yield send' + '-' * 10)
N = 20
sfib = stupidFib(N)
fibRes = next(sfib)

while True:
    print(fibRes)
    try:
        fibRes = sfib.send(random.uniform(0, 0.5))
    except StopIteration:
        break
