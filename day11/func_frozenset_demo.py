# http://www.runoob.com/python/python-func-frozenset.html
# TODO;Python frozenset() 函数

"""
描述
frozenset() 返回一个冻结的集合，冻结后集合不能再添加或删除任何元素。

语法
frozenset() 函数语法：

class frozenset([iterable])
参数
iterable -- 可迭代的对象，比如列表、字典、元组等等。
返回值
返回新的 frozenset 对象，如果不提供任何参数，默认会生成空集合。

实例
以下实例展示了 frozenset() 的使用方法：

"""

a = frozenset(range(10))  # 生成一个新的不可变集合
print(a)
# 不可修改
# a[0]=111
# 不可删除
# del a[0]

