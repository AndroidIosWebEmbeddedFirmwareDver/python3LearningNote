# http://www.runoob.com/python/python-func-repr.html
# TODO;Python repr() 函数

"""
描述
repr() 函数将对象转化为供解释器读取的形式。

语法
以下是 repr() 方法的语法:

repr(object)
参数
object -- 对象。
返回值
返回一个对象的 string 格式。

实例
以下展示了使用 repr() 方法的实例：
"""

s = 'RUNOOB'

print(s)
print(repr(s))

dict = {'runoob': 'runoob.com', 'google': 'google.com'};

print(dict)
print(repr(dict))
