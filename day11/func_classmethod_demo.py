# http://www.runoob.com/python/python-func-classmethod.html
# TODO;Python classmethod 修饰符

"""
描述
classmethod 修饰符对应的函数不需要实例化，不需要 self 参数，
但第一个参数需要是表示自身类的 cls 参数，可以来调用类的属性，
类的方法，实例化对象等。

语法
classmethod 语法：

classmethod
参数
无。
返回值
返回函数的类方法。

实例
以下实例展示了 classmethod 的使用方法：
"""


class A(object):
    bar = 1

    def func1(self):
        print('foo')

    @classmethod
    def func2(cls):
        print('func2')
        print(cls.bar)
        cls().func1()  # 调用 foo 方法


A.func2()  # 不需要实例化
