# http://www.runoob.com/python/python-func-hasattr.html
# TODO;Python hasattr() 函数

"""
描述
hasattr() 函数用于判断对象是否包含对应的属性。

语法
hasattr 语法：

hasattr(object, name)
参数
object -- 对象。
name -- 字符串，属性名。
返回值
如果对象有该属性返回 True，否则返回 False。

实例
以下实例展示了 hasattr 的使用方法：
"""


class Coordinate:
    x = 10
    y = -5
    z = 0


point1 = Coordinate()
print(hasattr(point1, 'x'))
print(hasattr(point1, 'y'))
print(hasattr(point1, 'z'))
print(hasattr(point1, 'no'))  # 没有该属性
