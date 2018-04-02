# http://www.runoob.com/python3/python3-func-reversed.html
# TODO;Python3 reversed 函数

"""
描述
reversed 函数返回一个反转的迭代器。

语法
以下是 reversed 的语法:

reversed(seq)
参数
seq -- 要转换的序列，可以是 tuple, string, list 或 range。
返回值
返回一个反转的迭代器。

实例
以下展示了使用 tuple 的实例：
"""

# 字符串
seqString = 'Runoob'
print(list(reversed(seqString)))

# 元组
seqTuple = ('R', 'u', 'n', 'o', 'o', 'b')
print(list(reversed(seqTuple)))

# range
seqRange = range(5, 9)
print(list(reversed(seqRange)))

# 列表
seqList = [1, 2, 4, 3, 5]
print(list(reversed(seqList)))



