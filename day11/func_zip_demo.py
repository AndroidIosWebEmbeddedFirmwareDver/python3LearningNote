# http://www.runoob.com/python/python-func-zip.html
# TODO;Python zip() 函数

"""
描述
zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。

如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。

语法
zip 语法：

zip([iterable, ...])
参数说明：

iterabl -- 一个或多个迭代器;
返回值
返回元组列表。

实例
以下实例展示了 zip 的使用方法：

"""

a = [1, 2, 2]
b = ['222', '2222', 123123123123]
c = [4, 5, 6, 7, 8]
zipped = zip(a, b)  # 打包为元组的列表
print(zipped)
print(tuple(zipped))

zipped = zip(a, c)  # 元素个数与最短的列表一致

print(zipped)
print(tuple(zipped))

zipped = zip(*zipped)  # 与 zip 相反，可理解为解压，返回二维矩阵式
print(zipped)

