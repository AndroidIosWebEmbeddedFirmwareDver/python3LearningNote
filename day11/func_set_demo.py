# http://www.runoob.com/python/python-func-set.html
# TODO;Python set() 函数

"""
描述
set() 函数创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等。

语法
set 语法：

class set([iterable])
参数说明：

iterable -- 可迭代对象对象；
返回值
返回新的集合对象。

实例
以下实例展示了 set 的使用方法：


"""

x = set('runoob')
y = set('google')

print(x, '\n', y)

# 交集
print(x & y)

# 并集

print(x | y)

# 差集

print(x - y)
