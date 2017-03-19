from multiprocessing import Process
import os

def run_proc(*args):
    vars = args
    print('Run child process %s...' % os.getpid())
    for (index, var) in enumerate(vars):
        print('the num.%d args is %s' % (index + 1, var))
if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test','num'))
    print('Child process will start')
    p.start()
    p.join()
    print('Chilld process end.')
