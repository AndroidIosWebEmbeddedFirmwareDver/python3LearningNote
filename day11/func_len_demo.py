# http://www.runoob.com/python3/python3-string-len.html
# TODO;Python3 len()方法

"""
描述
Python len() 方法返回对象（字符、列表、元组等）长度或项目个数。

语法
len()方法语法：

len( s )
参数
s -- 对象。
返回值
返回对象长度。

实例
以下实例展示了 len() 的使用方法：
"""

# 字符串
print(len('aaaaaaaaa'))
# list
print(len([1, 1, 1, 1, 1, 2, 3, 3, 2, 13, ]))
# tuple
print(len((1, 2, 2, 3, 2, 344, 3, 43, 4, 1, 23, 213, 134)))
# dict
print(len({'1': 1, "2": 2}))
