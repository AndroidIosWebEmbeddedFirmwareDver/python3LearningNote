# http://www.runoob.com/python/python-func-id.html
# TODO;Python id() 函数

"""
描述
id() 函数用于获取对象的内存地址。

语法
id 语法：

id([object])
参数说明：

object -- 对象。
返回值
返回对象的内存地址。

实例
以下实例展示了 id 的使用方法：

"""
a = 'runoob'
print(id(a))

b = 1

print(id(b))

c = 1
print(id(c))

# id(b)、id(c) 取得的内存地址一致，因为同一值会被存贮在相同的堆内存，b、c只是一个指向值的指针变量
