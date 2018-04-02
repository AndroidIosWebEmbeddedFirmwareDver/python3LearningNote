# http://www.runoob.com/python/python-func-dict.html
# TODO;Python dict() 函数

"""
描述
dict() 函数用于创建一个字典。

语法
dict 语法：

class dict(**kwarg)
class dict(mapping, **kwarg)
class dict(iterable, **kwarg)
参数说明：

**kwargs -- 关键字
mapping -- 元素的容器。
iterable -- 可迭代对象。
返回值
返回一个字典。

实例
以下实例展示了 dict 的使用方法：

"""
# 创建空字典
print(dict())

# 传入关键字
print(dict(a='1', b='c'))

# 映射函数方式来构造字典
print(dict(zip(['one', 'two', 'three'], [1, 2, 3])))

# 映射函数方式来构造字典
print(dict([('one', 1), ('two', 2), ('three', 3)]))
