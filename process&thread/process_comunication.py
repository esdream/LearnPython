from multiprocessing import Process, Queue
import os, time, random

# 写数据进程执行的代码
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('put %s to queue...' % value)
        q.put(value)
        # time.sleep(random.random())

# 读数据进程执行的代码
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

if __name__ == '__main__':
    # 父进程创建Queue, 并传递给各个子进程
    q = Queue()
    pwrite = Process(target=write, args=(q,))
    pread = Process(target=read, args=(q,))

    pwrite.start()
    pread.start()
    pwrite.join()
    pread.terminate()

    print('Parent Process has finished')
