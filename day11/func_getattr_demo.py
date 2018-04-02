# http://www.runoob.com/python/python-func-getattr.html
# TODO;Python getattr() 函数

"""
描述
getattr() 函数用于返回一个对象属性值。

语法
getattr 语法：

getattr(object, name[, default])
参数
object -- 对象。
name -- 字符串，对象属性。
default -- 默认返回值，如果不提供该参数，在没有对应属性时，将触发 AttributeError。
返回值
返回对象属性值。

实例
以下实例展示了 getattr 的使用方法：


"""


class A(object):
    bar = 1


a = A()
print(getattr(a, 'bar'))

print(bin(a.bar))

setattr(a, 'bar', 6778896457687)
print(getattr(a, 'bar'))
print(getattr(a, 'bar'))

print(bin(a.bar))


