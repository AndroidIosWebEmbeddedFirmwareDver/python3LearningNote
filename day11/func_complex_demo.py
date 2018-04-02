# http://www.runoob.com/python/python-func-complex.html
# TODO;Python complex() 函数

"""
描述
complex() 函数用于创建一个值为 real + imag * j 的复数或者转化一个字符串或数为复数。

如果第一个参数为字符串，则不需要指定第二个参数。。

语法
complex 语法：

class complex([real[, imag]])
参数说明：

real -- int, long, float或字符串；
imag -- int, long, float；
返回值
返回一个复数。

实例
以下实例展示了 complex 的使用方法：

"""

print(complex(1, 2))
print(complex(1))  # 数字
print(complex("1"))  # 当做字符串处理
# 注意：这个地方在"+"号两边不能有空格，也就是不能写成"1 + 2j"，应该是"1+2j"，否则会报错
print(complex("1+2j"))
