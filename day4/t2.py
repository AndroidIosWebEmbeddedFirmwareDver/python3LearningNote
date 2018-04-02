
#TODO;Tup To List
# tup1=('1',2,'3')
# print(list(tup1))

# TODO;Python3 元组
# """
# Python 的元组与列表类似，不同之处在于元组的元素不能修改。
#
# 元组使用小括号，列表使用方括号。
#
# 元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。
#
# 如下实例：
#
# tup1 = ('Google', 'Runoob', 1997, 2000);
# tup2 = (1, 2, 3, 4, 5 );
# tup3 = "a", "b", "c", "d";
# 创建空元组
#
# tup1 = ();
# 元组中只包含一个元素时，需要在元素后面添加逗号，否则括号会被当作运算符使用：
#
# >>> tup1 = (50)
# >>> type(tup1)     # 不加逗号，类型为整型
# <class 'int'>
#
# >>> tup1 = (50,)
# >>> type(tup1)     # 加上逗号，类型为元组
# <class 'tuple'>
# 元组与字符串类似，下标索引从0开始，可以进行截取，组合等。
#
#
#
# """


# TODO;访问元组
#
# tup1=('asdasd','1212',123123)
# tup2=(123123134,'1asdb')
#
# print(tup1)
# print(tup2)
# print(tup1[:1])
#



# TODO;修改元组
# """
# 元组中的元素值是不允许修改的，但我们可以对元组进行连接组合，如下实例:
# """
#
# tup1=(2,2,2,2)
# tup2=(1,12,21)
# print(tup1+tup2)

#TODO;删除元组
# """
# 元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组，如下实例:
# """
# tup1=(2,2,3)
# tup2=(1,1,2)
#
# print(tup1)
# del  tup1
# print(tup1)


# TODO;元组运算符
#
# """
# 与字符串一样，元组之间可以使用 + 号和 * 号进行运算。这就意味着他们可以组合和复制，运算后会生成一个新的元组。
#
# Python 表达式	结果	描述
# len((1, 2, 3))	3	计算元素个数
# (1, 2, 3) + (4, 5, 6)	(1, 2, 3, 4, 5, 6)	连接
# ('Hi!',) * 4	('Hi!', 'Hi!', 'Hi!', 'Hi!')	复制
# 3 in (1, 2, 3)	True	元素是否存在
# for x in (1, 2, 3): print x,	1 2 3	迭代
#
# """
#
# tup1=(1,2,3,4,5)
#
# print("""计算元素个数""",len(tup1))
# print("""连接""",tup1+(6,7,8,9,))
# print("""复制""",tup1*10+(6,7,8,9,))
# print("""元素是否存在""",'1' in tup1)
# print("""元素是否不存在""",'1' not in tup1)
# # 迭代
# for x in tup1:
#     print(x)
#

# TODO;元组索引，截取
# tup1=(1,2,3,4)
#
# print(tup1[:3])
# print(tup1[3])
# print(tup1[-3])

# TODO;元组内置函数
#
# """
# Python元组包含了以下内置函数
#
# 序号	方法及描述	实例
# 1	len(tuple)
# 计算元组元素个数。
# >>> tuple1 = ('Google', 'Runoob', 'Taobao')
# >>> len(tuple1)
# 3
# >>>
# 2	max(tuple)
# 返回元组中元素最大值。
# >>> tuple2 = ('5', '4', '8')
# >>> max(tuple2)
# '8'
# >>>
# 3	min(tuple)
# 返回元组中元素最小值。
# >>> tuple2 = ('5', '4', '8')
# >>> min(tuple2)
# '4'
# >>>
# 4	tuple(seq)
# 将列表转换为元组。
# >>> list1= ['Google', 'Taobao', 'Runoob', 'Baidu']
# >>> tuple1=tuple(list1)
# >>> tuple1
# ('Google', 'Taobao', 'Runoob', 'Baidu')
#
# """
# list1=[1,1,1,1,1,1]
# print(tuple(list1))



