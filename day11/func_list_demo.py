# http://www.runoob.com/python3/python3-att-list-list.html
# TODO;Python3 List list()方法

"""
描述
list() 方法用于将元组转换为列表。

注：元组与列表是非常类似的，区别在于元组的元素值不能修改，元组是放在括号中，列表是放于方括号中。

语法
list()方法语法：

list( seq )
参数
list -- 要转换为列表的元组。
返回值
返回列表。

实例
以下实例展示了 list()函数的使用方法：
"""

aTuple = (123, 'Google', 'Runoob', 'Taobao')
list1 = list(aTuple)
print("列表元素 : ", list1)

str = "Hello World"
list2 = list(str)
print("列表元素 : ", list2)
