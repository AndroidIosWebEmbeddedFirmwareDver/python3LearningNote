# http://www.runoob.com/python/att-string-format.html
# TODO;Python format 格式化函数


"""
Python2.6 开始，新增了一种格式化字符串的函数 str.format()，它增强了字符串格式化的功能。

基本语法是通过 {} 和 : 来代替以前的 % 。

format 函数可以接受不限个参数，位置可以不按顺序。

实例
"""
print("{} {}".format("hello", "world"))  # 不设置指定位置，按默认顺序

print("{0} {1}".format("hello", "world"))  # 设置指定位置

print("{1} {0} {1}".format("hello", "world"))  # 设置指定位置
