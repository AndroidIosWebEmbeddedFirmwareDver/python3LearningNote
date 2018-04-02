

# http://www.runoob.com/python/python-func-__import__.html
# TODO;Python __import__() 函数

"""
描述
__import__() 函数用于动态加载类和函数 。

如果一个模块经常变化就可以使用 __import__() 来动态载入。

语法
__import__ 语法：

__import__(name[, globals[, locals[, fromlist[, level]]]])
参数说明：

name -- 模块名
返回值
返回元组列表。

实例
以下实例展示了 __import__ 的使用方法：
"""

import os

print('在 a.py 文件中 %s' % id(os))
