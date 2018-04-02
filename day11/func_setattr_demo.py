# http://www.runoob.com/python/python-func-setattr.html
# TODO;Python setattr() 函数

"""
描述
setattr 函数对应函数 getatt()，用于设置属性值，该属性必须存在。

语法
setattr 语法：

setattr(object, name, value)
参数
object -- 对象。
name -- 字符串，对象属性。
value -- 属性值。
返回值
无。

实例
以下实例展示了 setattr 的使用方法：

"""


class A(object):
    bar = 1


a = A()

print(getattr(a, 'bar'))
setattr(a, 'bar', 123)
print(getattr(a, 'bar'))
