# http://www.runoob.com/python/python-func-iter.html
# TODO;Python iter() 函数

"""

描述
iter() 函数用来生成迭代器。

语法
以下是 iter() 方法的语法:

iter(object[, sentinel])
参数
object -- 支持迭代的集合对象。
sentinel -- 如果传递了第二个参数，则参数 object 必须是一个可调用的对象
（如，函数），此时，iter 创建了一个迭代器对象，每次调用这个迭代器对象的__next__()方法时，都会调用 object。
打开模式
返回值
迭代器对象。

实例
"""

li = ['123123', 12, 123, 123, 123, 13]

for x in iter(li):
    print(x, end=' ')

print('\n')
stttr = '7618899678768798hjdgvhabhisdvahsdadsuggasdg'

for x in iter(stttr):
    print(x, end=' ')
