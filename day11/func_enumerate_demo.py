# http://www.runoob.com/python3/python3-func-enumerate.html
# TODO;Python3 enumerate() 函数

"""
描述
enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个
索引序列，同时列出数据和数据下标，一般用在 for 循环当中。

语法
以下是 enumerate() 方法的语法:

enumerate(sequence, [start=0])
参数
sequence -- 一个序列、迭代器或其他支持迭代对象。
start -- 下标起始位置。
返回值
返回 enumerate(枚举) 对象。

实例
以下展示了使用 enumerate() 方法的实例：
"""

seasons = ['Spring', 'Summer', 'Fall', 'Winter']

print(list(enumerate(seasons)))

print(list(enumerate(seasons, start=1)))  # 小标从 1 开始

# 普通的 for 循环
i = 0
seq = ['one', 'two', 'three']
for element in seq:
    print(i, seq[i])
    i += 1

# for 循环使用 enumerate

seq = ['one', 'two', 'three']
for i, element in enumerate(seq):
    print(i, seq[i])

# 遍历字符串
seq = '12312312321adsasdasdad'

for i, element in enumerate(seq):
    print(i, seq[i])
