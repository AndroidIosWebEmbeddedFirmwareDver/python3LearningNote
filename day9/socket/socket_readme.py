
# TODO;Socket
"""
什么是 Socket?
Socket又称"套接字"，应用程序通常通过"套接字"向网络发出请求或者应答网络请求，使主机间或者一台计算机上的进程间可以通讯。
"""

# socket()函数

"""
Python 中，我们用 socket（）函数来创建套接字，语法格式如下：

socket.socket([family[, type[, proto]]])
参数
family: 套接字家族可以使AF_UNIX或者AF_INET
type: 套接字类型可以根据是面向连接的还是非连接分为SOCK_STREAM或SOCK_DGRAM
protocol: 一般不填默认为0.

"""
# A DEMO

import socket

if __name__ == '__main__':
    socket=socket.socket()
    print(socket)

