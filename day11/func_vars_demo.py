# http://www.runoob.com/python/python-func-vars.html

# TODO;Python vars() 函数

"""
描述
vars() 函数返回对象object的属性和属性值的字典对象。

语法
vars() 函数语法：

vars([object])
参数
object -- 对象
返回值
返回对象object的属性和属性值的字典对象，如果没有参数，就打印当前调用位置的属性和属性值 类似 locals()。

实例
以下实例展示了 vars() 的使用方法：
"""

print(vars())


class AAA(object):
    """"""


print(vars(AAA))
