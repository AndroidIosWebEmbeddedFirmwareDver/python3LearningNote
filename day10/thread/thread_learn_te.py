# TODO;开始学习Python线程

"""
Python中使用线程有两种方式：函数或者用类来包装线程对象。

函数式：调用 _thread 模块中的start_new_thread()函数来产生新线程。语法如下:

_thread.start_new_thread ( function, args[, kwargs] )
参数说明:

function - 线程函数。
args - 传递给线程函数的参数,他必须是个tuple类型。
kwargs - 可选参数。

实例：
"""

import time
import _thread


# 为线程定义一个执行函数
def print_time(threadName, delay):
    """"""
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print('%s: %s' % (threadName, time.ctime(time.time())))


# 执行函数
def done():
    """"""
    # 创建两个线程
    try:
        _thread.start_new_thread(print_time, ("Thread-1", 2,))
        _thread.start_new_thread(print_time, ("Thread-2", 4,))
    except Exception as e:
        print("Error: 无法启动线程,{0}".format(e))

    while 1:
        pass


if __name__ == '__main__':
    done()
