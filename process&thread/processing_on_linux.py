import os

print('Process %s start...' % os.getpid())

fork_PID = os.fork()

if fork_PID == 0:
    print('当前进程: %s, 父进程: %s, fork_PID: %s' % (os.getpid(), os.getppid(), fork_PID))
else:
    print('当期进程: %s, 创建了子进程: %s' % (os.getpid(), fork_PID))
