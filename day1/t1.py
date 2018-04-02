#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-

# python3基础语法


# 1.保留字------------------
"""
# 保留字

"""
print('1.保留字------------------')
import keyword

print(keyword.kwlist);

# 2.注解------------------
# 第一个注释
# 第二个注释

print('2.注解------------------')
'''
第三注释
第四注释
'''

"""
第五注释
第六注释
"""

# 3.行与缩进------------------

print('3.行与缩进------------------')
if True:
    print('True')
else:
    print('False')
"""
if True:
    print ("Answer")
    print ("True")
else:
    print ("Answer")
  print ("False")    # 缩进不一致，会导致运行错误
"""

# 4.多行语句------------------

print('4.多行语句------------------')
a = 1313 + \
    12123
print('a=', a)

# 5.数据类型------------------

# python中数有四种类型：整数、长整数、浮点数和复数。
#
# 整数， 如 1
# 长整数 是比较大的整数
# 浮点数 如 1.23、3E-2
# 复数 如 1 + 2j、 1.1 + 2.2j

print('5.数据类型------------------')

# 6.字符串------------------
# python中单引号和双引号使用完全相同。
# 使用三引号('''或""")可以指定一个多行字符串。
# 转义符 '\'
# 自然字符串， 通过在字符串前加r或R。 如 r"this is a line with \n" 则\n会显示，并不是换行。
# python允许处理unicode字符串，加前缀u或U， 如 u"this is an unicode string"。
# 字符串是不可变的。
# 按字面意义级联字符串，如"this " "is " "string"会被自动转换为this is string。

print('6.字符串------------------')

a = 'aaaaaaaa';
b = "aaaaaaa";
c = """
    这是一个段落
    我是一个段落
    我是哦
"""

print('a=>', a)
print('b=>', b)
print('c=>', c)

# 7.空行------------------
'''
函数之间或类的方法之间用空行分隔，表示一段新的代码的开始。类和函数入口之间也用一行空行分隔，以突出函数入口的开始。

空行与代码缩进不同，空行并不是Python语法的一部分。书写时不插入空行，Python解释器运行也不会出错。但是空行的作用在于分隔两段不同功能或含义的代码，便于日后代码的维护或重构。

记住：空行也是程序代码的一部分。
'''

print('7.空行------------------')

# 8.等待用户输入------------------
'''
input
'''

print('8.等待用户输入------------------')

print('请随意输入，我也不会管，你输入的是啥。')
input('\n\n按下 enter 键后退出。\n')

# 9.同一行显示多条语句------------------
'''
Python可以在同一行中使用多条语句，语句之间使用分号(;)分割，以下是一个简单的实例：
'''
print('9.同一行显示多条语句------------------')

import sys;

x = 'runoob';
sys.stdout.write(x + '\n')

# 10.多个语句构成代码组------------------
'''
缩进相同的一组语句构成一个代码块，我们称之代码组。

像if、while、def和class这样的复合语句，首行以关键字开始，以冒号( : )结束，该行之后的一行或多行代码构成代码组。

我们将首行及后面的代码组称为一个子句(clause)。

如下实例：
if expression : 
   suite
elif expression : 
   suite 
else : 
   suite
   
'''
print('10.多个语句构成代码组------------------')

a = 10
if a == 1:
    print(0)
elif a == 2:
    print(1)
else:
    print(2)

#
#
#
# 11.Print 输出------------------
'''
print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""：
'''
#
print('11.Print 输出------------------')
#
x = "a"
y = "b"
# 换行输出
print(x)
print(y)

print('---------')
# 不换行输出
print(x, end=" ")
print(y, end=" ")
print()

#
#
#
# 12.import 与 from...import出------------------
'''
在 python 用 import 或者 from...import 来导入相应的模块。

将整个模块(somemodule)导入，格式为： import somemodule

从某个模块中导入某个函数,格式为： from somemodule import somefunction

从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc

将某个模块中的全部函数导入，格式为： from somemodule import *

'''
#
print('12.import 与 from...import------------------')
#

# 导入 sys 模块
import sys

print('================Python import mode==========================');
print('命令行参数为:')
for i in sys.argv:
    print(i)
print('\n python 路径为', sys.path)

# 导入 sys 模块的 argv,path 成员
from sys import argv, path  # 导入特定的成员

print('================python from import===================================')
print('path:', path)  # 因为已经导入path成员，所以此处引用时不需要加sys.path




#
#
#
# 13.命令行参数------------------
'''
很多程序可以执行一些操作来查看一些基本信息，Python可以使用-h参数查看各参数帮助信息：
$ python -h
usage: python [option] ... [-c cmd | -m mod | file | -] [arg] ...
Options and arguments (and corresponding environment variables):
-c cmd : program passed in as string (terminates option list)
-d     : debug output from parser (also PYTHONDEBUG=x)
-E     : ignore environment variables (such as PYTHONPATH)
-h     : print this help message and exit

[ etc. ]

'''
#
print('13.命令行参数------------------')
#
print('http://www.runoob.com/python3/python3-command-line-arguments.html')