# http://www.runoob.com/python/python-func-callable.html
# TODO;http://www.runoob.com/python/python-func-callable.html

"""
描述
callable() 函数用于检查一个对象是否是可调用的。如果返回True，object仍然可能调用失败；

但如果返回False，调用对象ojbect绝对不会成功。

对于函数, 方法, lambda 函式, 类, 以及实现了 __call__ 方法的类实例, 它都返回 True。

语法
callable()方法语法：

callable(object)
参数
object -- 对象
返回值
可调用返回 True，否则返回 False。

实例
以下实例展示了 callable() 的使用方法：
"""

print(callable(0))  # 不能调用

print(callable(print))  # 可以调用
