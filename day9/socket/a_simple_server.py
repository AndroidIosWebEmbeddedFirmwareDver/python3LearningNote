# TODO;服务端
# 我们使用 socket 模块的 socket 函数来创建一个 socket 对象。socket 对象可以通过调用其他函数来设置一个 socket 服务。
#
# 现在我们可以通过调用 bind(hostname, port) 函数来指定服务的 port(端口)。
#
# 接着，我们调用 socket 对象的 accept 方法。该方法等待客户端的连接，并返回 connection 对象，表示已连接到客户端。
#
# 完整代码如下：

# 导入 socket、sys 模块
import socket
import sys

# 创建 socket 对象
serversocket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
host = socket.gethostname()

port = 9999

print('server->\n{0}:{1}'.format(host, port))

# 绑定端口号
serversocket.bind((host, port))

# 设置最大连接数，超过后排队
serversocket.listen(5)

while True:
    # 建立客户端连接
    clientsocket, addr = serversocket.accept()

    print("连接地址: %s" % str(addr))

    msg = 'A MSG FROM SREVER 欢迎访问！' + "\r\n"
    clientsocket.send(msg.encode('utf-8'))
    clientsocket.close()
