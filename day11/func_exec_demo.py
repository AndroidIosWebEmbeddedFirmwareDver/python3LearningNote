# http://www.runoob.com/python3/python3-func-exec.html
# TODO;Python3 exec 函数

"""
描述
exec 执行储存在字符串或文件中的 Python 语句，相比于 eval，exec可以执行更复杂的 Python 代码。

语法
以下是 exec 的语法:

exec(object[, globals[, locals]])
参数
object：必选参数，表示需要被指定的Python代码。它必须是字符串或code对象。如果object是一个字符串，
        该字符串会先被解析为一组Python语句，然后在执行（除非发生语法错误）。如果object是一个code对象，那么它只是被简单的执行。
globals：可选参数，表示全局命名空间（存放全局变量），如果被提供，则必须是一个字典对象。
locals：可选参数，表示当前局部命名空间（存放局部变量），如果被提供，可以是任何映射对象。如果该参数被忽略，
        那么它将会取与globals相同的值。
返回值
exec 返回值永远为 None。

实例
以下展示了使用 exec 的实例：


"""

# 单行语句字符串
exec('print("Hello World")')
#  多行语句字符串
exec("""for i in range(5):
            print ("iter time: %d" % i)
            """)

# 实例 2
x = 10
expr = """
z = 30
sum = x + y + z
print(sum)
"""


def func():
    y = 20
    exec(expr)
    exec(expr, {'x': 1, 'y': 2})
    exec(expr, {'x': 1, 'y': 2}, {'y': 3, 'z': 4})


func()
