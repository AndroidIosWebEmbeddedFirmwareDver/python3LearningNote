# http://www.runoob.com/python/python-func-compile.html
# TODO;Python compile() 函数

"""
描述
compile() 函数将一个字符串编译为字节代码。

语法
以下是 compile() 方法的语法:

compile(source, filename, mode[, flags[, dont_inherit]])
参数
source -- 字符串或者AST（Abstract Syntax Trees）对象。。
filename -- 代码文件名称，如果不是从文件读取代码则传递一些可辨认的值。
mode -- 指定编译代码的种类。可以指定为 exec, eval, single。
flags -- 变量作用域，局部命名空间，如果被提供，可以是任何映射对象。。
flags和dont_inherit是用来控制编译源码时的标志
返回值
返回表达式执行结果。
"""

str = "for i in range(0,10): print(i)"
c = compile(str, '', 'exec')  # 编译为字节代码对象
print(c)

exec(c)

str = "3 * 4 + 5"
a = compile(str, '', 'eval')
eval(a)
