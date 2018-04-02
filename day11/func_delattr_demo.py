# http://www.runoob.com/python/python-func-delattr.html

# TODO;Python delattr() 函数

"""
描述
delattr 函数用于删除属性。

delattr(x, 'foobar') 相等于 del x.foobar。

语法
setattr 语法：

delattr(object, name)
参数
object -- 对象。
name -- 必须是对象的属性。
返回值
无。

实例
以下实例展示了 delattr 的使用方法：
"""


class Coordinate:
    x = 10
    y = -5
    z = 0


point1 = Coordinate()

print('x = ', point1.x)
print('y = ', point1.y)
print('z = ', point1.z)

delattr(Coordinate, 'z')

print('--删除 z 属性后--')
print('x = ', point1.x)
print('y = ', point1.y)

# 触发错误
print('z = ', point1.z)


