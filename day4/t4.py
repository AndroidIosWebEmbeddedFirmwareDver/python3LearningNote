# TODO;Python3 编程第一步

"""
在前面的教程中我们已经学习了一些 Python3 的基本语法知识，下面我们尝试来写一个斐波纳契数列。

"""
#
# # 斐波纳契数列
# a, b = 0, 1
#
# while b < 100000000:
#     print('a=',a,'斐b=',b)
#     a, b = b, a + b

# TODO;end 关键字
"""
关键字end可以用于将结果输出到同一行，或者在输出的末尾添加不同的字符，实例如下：
"""
# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
a, b = 0, 1
while b < 1000:
    print(b, end=',')
    a, b = b, a+b