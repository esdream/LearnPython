import socket
import threading
import time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 9999))
# 绑定端口
print('Bind UDP on 9999....')
while True:
    # 接收数据
    data, addr = s.recvfrom(1024)
    print(addr)
    print('Received from %s: %s.' % addr)
    s.sendto(b'Hello, %s!' % data, addr)
