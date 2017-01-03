from multiprocessing import Process
import os

def run_proc(*args):
    var = args
    print('Run child process %s (%s)...' % (var[0], os.getpid()))
if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test','num'))
    print('Child process will start')
    p.start()
    p.join()
    print('Chilld process end.')
