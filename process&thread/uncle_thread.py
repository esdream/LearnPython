# -*- encoding: utf-8 -*-
import time, threading, os, random

g_val = 0
g_lock = threading.Lock()

def workthread(times = 10):
    global g_val
    global g_lock

    count = 0
    while count < times:
        g_lock.acquire()
        try:
            g_val += 1
            print('thread [%s] set g_val is [%d]' % (threading.current_thread().name, g_val))
        finally:
            g_lock.release()
        time.sleep(1)
        count += 1

    print('thread [%s] exit.' % threading.current_thread().name)

if __name__ == '__main__':
    print('Process %d running...' % os.getpid())
    threads = []
    for i in range(3):
        t = threading.Thread(target=workthread)
        print('Process %s will create thread[%s]' % (os.getpid(), t.name))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print('Process %d all sub threads finished.' % os.getpid())
