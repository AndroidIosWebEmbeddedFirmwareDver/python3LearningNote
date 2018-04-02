# http://www.runoob.com/python/python-func-memoryview.html
# TODO;Python memoryview() 函数

"""
描述
memoryview() 函数返回给定参数的内存查看对象(Momory view)。

所谓内存查看对象，是指对支持缓冲区协议的数据进行包装，在不需要复制对象基础上允许Python代码访问。

语法
memoryview 语法：

memoryview(obj)
参数说明：

obj -- 对象
返回值
返回元组列表。

实例
以下实例展示了 memoryview 的使用方法：
"""

"""
Python2.x 应用：
>>>v = memoryview('abcefg')
>>> v[1]
'b'
>>> v[-1]
'g'
>>> v[1:4]
<memory at 0x77ab28>
>>> v[1:4].tobytes()
'bce'
"""

"""
Python3.x 应用：
"""
v = memoryview(bytearray("abcefg", 'utf-8'))
print(v[1])
print(v[-1])
print(v[1:4])
print(v[1:4].tobytes())

print(v)
print(v.tobytes())
