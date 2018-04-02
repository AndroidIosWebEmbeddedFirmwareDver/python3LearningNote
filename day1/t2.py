# Python3 基本数据类型


#
#
#
# 01.变量声明赋值------------------
"""
Python 中的变量不需要声明。每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。

在 Python 中，变量就是变量，它没有类型，我们所说的"类型"是变量所指的内存中对象的类型。

等号（=）用来给变量赋值。

等号（=）运算符左边是一个变量名,等号（=）运算符右边是存储在变量中的值。例如：

"""
#
print('01.变量声明赋值------------------')
#

counter = 100  # 整型变量
miles = 1000.0  # 浮点型变量
name = "runoob"  # 字符串

print(counter)
print(miles)
print(name)

#
#
#
# 02.多个变量赋值------------------
"""
Python允许你同时为多个变量赋值。例如：

a = b = c = 1
以上实例，创建一个整型对象，值为1，三个变量被分配到相同的内存空间上。

您也可以为多个对象指定多个变量。例如：

a, b, c = 1, 2, "runoob"
以上实例，两个整型对象 1 和 2 的分配给变量 a 和 b，字符串对象 "runoob" 分配给变量 c。

"""
#
print('02.多个变量赋值------------------')
#

k1, k2, k3 = 122, 2323.123123, 'asdaashdhjaisbdih12u3'

print('k1=', k1, '\nk2=', k2, '\nk3=', k3)

#
#
#
# 03.标准数据类型------------------
"""
Python3 中有六个标准的数据类型：

Number（数字）
String（字符串）
List（列表）
Tuple（元组）
Sets（集合）
Dictionary（字典）

"""
#
print('03.标准数据类型------------------')
#


#
#
#
# 04.Number------------------
"""
Number（数字）
Python3 支持 int、float、bool、complex（复数）。

在Python 3里，只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。

像大多数语言一样，数值类型的赋值和计算都是很直观的。

内置的 type() 函数可以用来查询变量所指的对象类型。
"""
#
print('04.Number------------------')
#

a, b, c, d = 112, 111.11111, False, 1212 + 2j

print(type(a), type(b), type(c), type(d))

print('a is a int Number? ', isinstance(a, int), '\n',
      'b is a float Number? ', isinstance(b, float), '\n',
      'c is a bool Number? ', isinstance(c, bool), '\n',
      'd is a complex Number? ', isinstance(d, complex))

#
#
#
# 04.Number------------------
"""
Number（数字）
Python3 支持 int、float、bool、complex（复数）。

在Python 3里，只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。

像大多数语言一样，数值类型的赋值和计算都是很直观的。

"""
#
print('04.Number------------------')
#

a, b, c, d = 112, 111.11111, False, 1212 + 2j

# 内置的 type() 函数可以用来查询变量所指的对象类型。

print(type(a), type(b), type(c), type(d))

# 此外还可以用 isinstance 来判断：
print('a is a int Number? ', isinstance(a, int), '\n',
      'b is a float Number? ', isinstance(b, float), '\n',
      'c is a bool Number? ', isinstance(c, bool), '\n',
      'd is a complex Number? ', isinstance(d, complex))
# 区别就是:type()不会认为子类是一种父类类型。isinstance()会认为子类是一种父类类型。

# 当你指定一个值时，Number 对象就会被创建：
var1 = 1
var2 = 10
# 您也可以使用del语句删除一些对象引用。
# del语句的语法是： del var1[,var2[,var3[....,varN]]]]

# 您可以通过使用del语句删除单个或多个对象。例如：
del var1
del a, b, c, d
# print(a) -->删除后再使用这里直接报错，NameError: name 'a' is not defined


#
#
#
# 05.数值运算------------------
"""
"""
#
print('05.数值运算------------------')
#

# +加法 -减法 *乘法 /除法 %取余 **乘方

print(13 + 5)  # 加法
print(14 - 6)  # 减法
print(15 * 7)  # 乘法
print(16 / 8)  # 除法，得到一个浮点数
print(17 // 9)  # 除法，得到一个整数
print(18 % 10)  # 取余
print(19 ** 11)  # 乘方

"""
注意：

1、Python可以同时为多个变量赋值，如a, b = 1, 2。
2、一个变量可以通过赋值指向不同类型的对象。
3、数值的除法（/）总是返回一个浮点数，要获取整数使用//操作符。
4、在混合计算时，Python会把整型转换成为浮点数。
"""

#
#
#
# 06.数值类型实例------------------
"""
Number（数字）
Python3 支持 int、float、bool、complex（复数）。

在Python 3里，只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。

像大多数语言一样，数值类型的赋值和计算都是很直观的。

"""
#
print('06.数值类型实例------------------')
#


#
#
#
# 07.String（字符串）------------------
"""
Python中的字符串用单引号(')或双引号(")括起来，同时使用反斜杠(\)转义特殊字符。

字符串的截取的语法格式如下：

变量[头下标:尾下标]
索引值以 0 为开始值，-1 为从末尾的开始位置。

加号 (+) 是字符串的连接符， 星号 (*) 表示复制当前字符串，紧跟的数字为复制的次数。实例如下：

"""
#
print('07.String（字符串）------------------')
#

str = 'Runoob'

print(str)  # 输出字符串
print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
print(str[0])  # 输出字符串第一个字符
print(str[2:5])  # 输出从第三个开始到第五个的字符
print(str[2:])  # 输出从第三个开始的后的所有字符
print(str * 2)  # 输出字符串两次
print(str + "TEST")  # 连接字符串

#
#
#
# 08.List（列表）------------------
"""
List（列表） 是 Python 中使用最频繁的数据类型。

列表可以完成大多数集合类的数据结构实现。列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓嵌套）。

列表是写在方括号([])之间、用逗号分隔开的元素列表。

和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表。

列表截取的语法格式如下：

变量[头下标:尾下标]
索引值以 0 为开始值，-1 为从末尾的开始位置。

加号（+）是列表连接运算符，星号（*）是重复操作。如下实例：
"""

#
print('08.List（列表）------------------')
#

list = [12312, '1123', 'asdadad', 'adad1231edasdqee2ewd']
tinylist = [123, 'runoob']

print(list)  # 输出完整列表
print(list[0])  # 输出列表第一个元素
print(list[1:3])  # 从第二个开始输出到第三个元素
print(list[2:])  # 输出从第三个元素开始的所有元素
print(tinylist * 2)  # 输出两次列表
print(list + tinylist)  # 连接列表

list[1] = 'thfcgjyuhkijthfgjyhkljygh'

print(list)  # 输出完整列表

"""
List内置了有很多方法，例如append()、pop()等等，这在后面会讲到。

注意：

1、List写在方括号之间，元素用逗号隔开。
2、和字符串一样，list可以被索引和切片。
3、List可以使用+操作符进行拼接。
4、List中的元素是可以改变的。

"""

#
#
#
# 09.Tuple（元组)------------------
"""
Tuple（元组）
元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号(())里，元素之间用逗号隔开。

元组中的元素类型也可以不相同：
"""

#
print('09.Tuple（元组) ------------------')
#

tuple = ('aaaashgjsvkjbjgachdv', 1231231, 'asdadasda', 1231364728)
tinytuple = (123, 'runoob')

print(tuple)  # 输出完整元组
print(tuple[0])  # 输出元组的第一个元素
print(tuple[1:3])  # 输出从第二个元素开始到第三个元素
print(tuple[2:])  # 输出从第三个元素开始的所有元素
print(tinytuple * 2)  # 输出两次元组
print(tuple + tinytuple)  # 连接元组

# tuple[0]='asdadad' # TypeError: 'tuple' object does not support item assignment 元组的元素不能修改值


"""
虽然tuple的元素不可改变，但它可以包含可变的对象，比如list列表。

构造包含 0 个或 1 个元素的元组比较特殊，所以有一些额外的语法规则：

tup1 = ()    # 空元组
tup2 = (20,) # 一个元素，需要在元素后添加逗号
string、list和tuple都属于sequence（序列）。

注意：

1、与字符串一样，元组的元素不能修改。
2、元组也可以被索引和切片，方法一样。
3、注意构造包含0或1个元素的元组的特殊语法规则。
4、元组也可以使用+操作符进行拼接。

"""

#
#
#
# 10.Set（集合）------------------
"""
集合（set）是一个无序不重复元素的序列。

基本功能是进行成员关系测试和删除重复元素。

可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。

创建格式：

parame = {value01,value02,...}
或者
set(value)

"""

#
print('10.Set（集合） ------------------')
#


student = {'lili', 'luci', 'tom', 'coche', 'door', 'lili'}
print(student)  # 输出集合，重复的元素被自动去掉

# 成员测试
if ('rose' in student):
    print('rose in student')
else:
    print('rose not in student')

# set可以进行集合运算

a = set('abracadabra')
b = set('alacazam')

print(a)

print(a - b)  # a和b的差集

print(a | b)  # a和b的并集

print(a & b)  # a和b的交集

print(a ^ b)  # a和b中不同时存在的元素

#
#
#
# 11.Dictionary（字典）------------------
"""
字典（dictionary）是Python中另一个非常有用的内置数据类型。

列表是有序的对象结合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。

字典是一种映射类型，字典用"{ }"标识，它是一个无序的键(key) : 值(value)对集合。

键(key)必须使用不可变类型。

在同一个字典中，键(key)必须是唯一的。

"""

#
print('11.Dictionary（字典）------------------')
#

mD1 = {}
mD1['gfhj'] = 'ghjbkhgvjbknghvjbkhgvjbkhgvjhgvjbhgvj'
mD1[1231233] = 678965787567865786879878679887689876
mD1[2] = 678965787567865786879878679887689876
mD1[1] = 'aaaaaaaa12222222'
mD1[1] = 'sadadadadaasdasdad'  # 由于字典要求key唯一性所以这里会重新赋值

print(mD1)

tinymD2 = {12222: 1231231231, 'adadada': 123132, '12312313': 'gyuhjyfghjygh'}

# print(mD1['one'])  # 输出键为 'one' 的值 # 会报错 KeyError: 'one'
print(mD1[2])  # 输出键为 2 的值
print(tinymD2)  # 输出完整的字典
print(tinymD2.keys())  # 输出所有键
print(tinymD2.values())  # 输出所有值

"""
构造函数 dict() 可以直接从键值对序列中构建字典如下：

实例
>>>dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])
{'Taobao': 3, 'Runoob': 1, 'Google': 2}
 
>>> {x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}
 
>>> dict(Runoob=1, Google=2, Taobao=3)
{'Taobao': 3, 'Runoob': 1, 'Google': 2}
另外，字典类型也有一些内置的函数，例如clear()、keys()、values()等。

注意：

1、字典是一种映射类型，它的元素是键值对。
2、字典的关键字必须为不可变类型，且不能重复。
3、创建空字典使用 { }。


"""
#dict 函数自动构建字典
print(dict([('gagsdgahid',11111),('asdadadad','dxtfcghjfyghjycghjkgchjgfchvjb')]))
print(dict({x: x**2 for x in (2, 4, 6)}))


#
#
#
# 12.Python数据类型转换------------------
"""
有时候，我们需要对数据内置的类型进行转换，数据类型的转换，你只需要将数据类型作为函数名即可。

以下几个内置的函数可以执行数据类型之间的转换。这些函数返回一个新的对象，表示转换的值。



函数	描述
int(x [,base])

将x转换为一个整数

float(x)

将x转换到一个浮点数

complex(real [,imag])

创建一个复数

str(x)

将对象 x 转换为字符串

repr(x)

将对象 x 转换为表达式字符串

eval(str)

用来计算在字符串中的有效Python表达式,并返回一个对象

tuple(s)

将序列 s 转换为一个元组

list(s)

将序列 s 转换为一个列表

set(s)

转换为可变集合

dict(d)

创建一个字典。d 必须是一个序列 (key,value)元组。

frozenset(s)

转换为不可变集合

chr(x)

将一个整数转换为一个字符

ord(x)

将一个字符转换为它的整数值

hex(x)

将一个整数转换为一个十六进制字符串

oct(x)

将一个整数转换为一个八进制字符串

"""

#
print('12.Python数据类型转换------------------')
#




