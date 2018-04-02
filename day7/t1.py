# # TODO;Python3 实例
#
# # # TODO;Python Hello World 实例
# #
# # print('Hello World!')
# #
#
# # # TODO;Python 数字求和
# #
# # # 输入
# # num1=input('请输入加数:')
# # num2=input('请输入被加数:')
# # # 求和
# #
# # sum=num1+num2
# #
# # print('数字 {0} 和 {1} 相加结果为： {2}'.format(num1, num2, sum))
#
# #
# # # TODO;Python 平方根
# #
# # num = float(input('请输入一个数：'))
# # num_sqrt = num ** 0.5
# #
# # print('%0.3f 的平方根为 %0.3f'%(num, num_sqrt))
# #
# #
# # import cmath
# #
# # num = int(input("请输入一个数字: "))
# # num_sqrt = cmath.sqrt(num)
# # print('{0} 的平方根为 {1:0.3f}+{2:0.3f}j'.format(num, num_sqrt.real, num_sqrt.imag))
#
#
# # # TODO;Python 二次方程
# #
# #
# # # 二次方程式 ax**2 + bx + c = 0
# # # a、b、c 用户提供
# #
# # # 导入 cmath(复杂数学运算) 模块
# # import cmath
# #
# # a = float(input('输入 a: '))
# # b = float(input('输入 b: '))
# # c = float(input('输入 c: '))
# #
# # # 计算
# # d = (b ** 2) - (4 * a * c)
# #
# # # 两种求解方式
# # sol1 = (-b - cmath.sqrt(d)) / (2 * a)
# # sol2 = (-b + cmath.sqrt(d)) / (2 * a)
# #
# # print('结果为 {0} 和 {1}'.format(sol1, sol2))
# #
# # import math
# #
# # a, b, c = input("请输入3个数字(空格分隔)：").split()
# # a = float(a)
# # b = float(b)
# # c = float(c)
# # d = (b ** 2) - (4 * a * c)
# # if a == 0 and b == 0 and c == 0:
# #     print("有无穷个解")
# # elif d >= 0:
# #     x1 = (-b - d / (2 * a))
# #     x2 = (-b + d / (2 * a))
# #     print('结果为：%.2f,%.2f' % (x1, x2));
# # else:
# #     print("无解")
#
#
# # TODO;Python 计算三角形的面积
# #
# # def params_input():
# #     global a, b, c
# #     a = float(input('输入三角形第一边长: '))
# #     b = float(input('输入三角形第二边长: '))
# #     c = float(input('输入三角形第三边长: '))
# #
# #
# # def params_area():
# #     """"""
# #     params_input()
# #     if a + b <= c:
# #         print('输入参数有误，请重新输入')
# #         params_area()
# #     else:
# #         # 计算半周长
# #         s = (a + b + c) / 2
# #
# #         # 计算面积
# #         area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
# #         print('三角形面积为 %0.2f' % area)
# #
# #
# # params_area()
#
# # TODO;Python 随机数生成
# # # 随机数字小游戏
# # import random
# #
# # i = 1
# # a = random.randint(0, 100)
# # b = int(input('请输入0-100中的一个数字\n然后查看是否与电脑一样：'))
# # while a != b:
# #     if a > b:
# #         print('你第%d输入的数字小于电脑随机数字' % i)
# #         b = int(input('请再次输入数字:'))
# #     else:
# #         print('你第%d输入的数字大于电脑随机数字' % i)
# #         b = int(input('请再次输入数字:'))
# #     i += 1
# # else:
# #     print('恭喜你，你第%d次输入的数字与电脑的随机数字%d一样' % (i, b))
#
#
# # TODO;Python 摄氏温度转华氏温度
# #
# #
# # try:
# #     # 用户输入摄氏温度
# #
# #     # 接收用户输入
# #     celsius = float(input('输入摄氏温度: '))
# #
# #     # 计算华氏温度
# #     fahrenheit = (celsius * 1.8) + 32
# #     print('%0.1f 摄氏温度转为华氏温度为 %0.1f ' % (celsius, fahrenheit))
# # except Exception as e:
# #     print(e)
# #
# #
#
#
# # TODO;Python 交换变量
# #
# # # 以下实例通过用户输入两个变量，并相互交换：
# # try:
# #     # 用户输入
# #
# #     x = input('输入 x 值: ')
# #     y = input('输入 y 值: ')
# #
# #     # 创建临时变量，并交换
# #     temp = x
# #     x = y
# #     y = temp
# #
# #     print('交换后 x 的值为: {}'.format(x))
# #     print('交换后 y 的值为: {}'.format(y))
# # except Exception as e:
# #     print(e)
# #
# # """
# # 以上实例中，我们创建了临时变量 temp ，并将 x 的值存储在 temp 变量中，接着将 y 值赋给 x，最后将 temp 赋值给 y 变量。
# #
# #
# # """
# #
# # try:
# #     # 用户输入
# #     x = input('输入 x 值：')
# #     y = input('输入 y 值：')
# #
# #     # 交换变量
# #     x, y = y, x
# #     print('交换后 x 的值为: {}'.format(x))
# #     print('交换后 y 的值为: {}'.format(y))
# #
# # except Exception as e:
# #     print(e)
#
#
# # Python if 语句
# # Document 对象参考手册 Python3 实例
# #
# # 以下实例通过使用 if...elif...else 语句判断数字是正数、负数或零：
# #
# # # -*- coding: UTF-8 -*-
# #
# # # Filename : test.py
# # # author by : www.runoob.com
# #
# # # 用户输入数字
# #
# # num = float(input("输入一个数字: "))
# # if num > 0:
# #    print("正数")
# # elif num == 0:
# #    print("零")
# # else:
# #    print("负数")
# # 执行以上代码输出结果为：
# #
# # $ python test.py
# # 输入一个数字: 3
# # 正数
# # 我们也可以使用内嵌 if 语句来实现：
# #
# # # -*- coding: UTF-8 -*-
# #
# # # Filename ：test.py
# # # author by : www.w3cschool.cc
# #
# # # 内嵌 if 语句
# #
# # num = float(input("输入一个数字: "))
# # if num >= 0:
# #    if num == 0:
# #        print("零")
# #    else:
# #        print("正数")
# # else:
# #    print("负数")
# # 执行以上代码输出结果为：
# #
# # $ python test.py
# # 输入一个数字: 0
# # 零
# # Document 对象参考手册 Python3 实例
# #
# #
# # # TODO;Python 判断字符串是否为数字
# #
# # def is_number(s):
# #     try:
# #         float(s)
# #         return True
# #     except ValueError:
# #         pass
# #
# #     try:
# #         import unicodedata
# #         unicodedata.numeric(s)
# #         return True
# #     except (TypeError, ValueError):
# #         pass
# #
# #     return False
# #
# #
# # # 测试字符串和数字
# # print(is_number('foo'))  # False
# # print(is_number('1'))  # True
# # print(is_number('1.3'))  # True
# # print(is_number('-1.37'))  # True
# # print(is_number('1e3'))  # True
# #
# # # 测试 Unicode
# # # 阿拉伯语 5
# # print(is_number('٥'))  # True
# # # 泰语 2
# # print(is_number('๒'))  # True
# # # 中文数字
# # print(is_number('四'))  # True
# # # 版权号
# # print(is_number('©'))  # False
#
#
# # TODO;Python 判断奇数偶数
# #
# # num =int(input('输入一个数字：'))
# #
# # if (num % 2)==0:
# #     print('{0}是一个偶数'.format(num))
# # else:
# #     print('{0}是一个基数'.format(num))
# #
#
# # # TODO;Python 判断闰年
# # year = int(input("输入一个年份: "))
# # if (year % 4) == 0:
# #     if (year % 100) == 0:
# #         if (year % 400) == 0:
# #             print("{0} 是闰年".format(year))  # 整百年能被400整除的是闰年
# #         else:
# #             print("{0} 不是闰年".format(year))
# #     else:
# #         print("{0} 是闰年".format(year))  # 非整百年能被4整除的为闰年
# # else:
# #     print("{0} 不是闰年".format(year))
# #
# #
#
#
# # # TODO;最大值函数
# #
# # # 最简单的
# # print(max(1, 2))
# # print(max('a', 'b'))
# #
# # # 也可以对列表和元组使用
# # print(max([1, 2]))
# # print(max((1, 2)))
# #
# # # 更多实例
# # print("80, 100, 1000 最大值为: ", max(80, 100, 1000))
# # print("-20, 100, 400最大值为: ", max(-20, 100, 400))
# # print("-80, -20, -10最大值为: ", max(-80, -20, -10))
# # print("0, 100, -400最大值为:", max(0, 100, -400))
#
#
# # TODO;Python 质数判断
#
#
# # 用户输入数字
# # num = int(input("请输入一个数字: "))
# #
# # # 质数大于 1
# # if num > 1:
# #     # 查看因子
# #     for i in range(2, num):
# #         if (num % i) == 0:
# #             print(num, "不是质数")
# #             print(i, "乘于", num // i, "是", num)
# #             break
# #     else:
# #         print(num, "是质数")
# #
# # # 如果输入的数字小于或等于 1，不是质数
# # else:
# #     print(num, "不是质数")
# #
# # # TODO;Python 输出指定范围内的素数
# #
# # # 输出指定范围内的素数
# #
# # # take input from the user
# # lower = int(input("输入区间最小值: "))
# # upper = int(input("输入区间最大值: "))
# #
# # for num in range(lower, upper + 1):
# #     # 素数大于 1
# #     if num > 1:
# #         for i in range(2, num):
# #             if (num % i) == 0:
# #                 break
# #         else:
# #             print(num)
# #
#
# # TODO;Python 阶乘实例
# #
# # # 通过用户输入数字计算阶乘
# #
# # # 获取用户输入的数字
# # num = int(input("请输入一个数字: "))
# # factorial = 1
# #
# # # 查看数字是负数，0 或 正数
# # if num < 0:
# #     print("抱歉，负数没有阶乘")
# # elif num == 0:
# #     print("0 的阶乘为 1")
# # else:
# #     for i in range(1, num + 1):
# #         factorial = factorial * i
# #     print("%d 的阶乘为 %d" % (num, factorial))
# #
# #
# #
# #
# # # TODO;Python 九九乘法表
# #
# #
# # for i in range(1,10):
# #     for j in range(1,i+1):
# #         print('{0}*{1}={2}\t'.format(i,j,i*j),end='')
# #     print()
#
# # TODO;Python 斐波那契数列
#
# # # 获取用户输入数据
# # nterms = int(input("你需要几项？"))
# #
# # # 第一和第二项
# # n1 = 0
# # n2 = 1
# # count = 2
# #
# # # 判断输入的值是否合法
# # if nterms <= 0:
# #     print("请输入一个正整数。")
# # elif nterms == 1:
# #     print("斐波那契数列：")
# #     print(n1)
# # else:
# #     print("斐波那契数列：")
# #     print(n1, ",", n2, end=" , ")
# #     while count < nterms:
# #         nth = n1 + n2
# #         print(nth, end=" , ")
# #         # 更新值
# #         n1 = n2
# #         n2 = nth
# #         count += 1
# #
#
#
# # TODO;Python 阿姆斯特朗数
# """
# 如果一个n位正整数等于其各位数字的n次方之和,则称该数为阿姆斯特朗数。 例如1^3 + 5^3 + 3^3 = 153。
#
# 1000以内的阿姆斯特朗数： 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407。
#
# 以下代码用于检测用户输入的数字是否为阿姆斯特朗数：
#
# """
#
# #
# # print(100//10)
# # # Python 检测用户输入的数字是否为阿姆斯特朗数
# #
# # # 获取用户输入的数字
# # num = int(input("请输入一个数字: "))
# #
# # # 初始化变量 sum
# # sum = 0
# # # 指数
# # n = len(str(num))
# #
# # # 检测
# # temp = num
# # while temp > 0:
# #     digit = temp % 10
# #     sum += digit ** n
# #     temp //= 10
# #
# # # 输出结果
# # if num == sum:
# #     print(num, "是阿姆斯特朗数")
# # else:
# #     print(num, "不是阿姆斯特朗数")
#
#
# # 获取指定期间内的阿姆斯特朗数
# #
# # # 获取用户输入数字
# # lower = int(input("最小值: "))
# # upper = int(input("最大值: "))
# #
# # for num in range(lower, upper + 1):
# #     # 初始化 sum
# #     sum = 0
# #     # 指数
# #     n = len(str(num))
# #
# #     # 检测
# #     temp = num
# #     while temp > 0:
# #         digit = temp % 10
# #         sum += digit ** n
# #         temp //= 10
# #
# #     if num == sum:
# #         print(num)
#
# # # TODO;Python 十进制转二进制、八进制、十六进制
# #
# # # 十进制转二进制
# # def tenToTwo(dec):
# #     """"""
# #     return bin(dec)
# #
# #
# # # 十进制转八进制
# # def tenToEight(dec):
# #     """"""
# #     return oct(dec)
# #
# #
# # # 十进制转十六进制
# # def tenToSixteen(dec):
# #     """"""
# #     return hex(dec)
# #
# #
# # # 输入
# # def numInputConvert():
# #     """"""
# #     dec = int(input('请输入要转换的数字：'))
# #
# #     print('转二进制：{0}'.format(tenToTwo(dec)))
# #     print('转八进制：{0}'.format(tenToEight(dec)))
# #     print('转十六进制：{0}'.format(tenToSixteen(dec)), end='\n\n')
# #     numInputConvert()
# #
# #
# # if __name__ == '__main__':
# #     numInputConvert()
#
#
# # TODO;Python ASCII码与字符相互转换
#
# #
# # #
# # def strToAscii(dec):
# #     """"""
# #     return ord(dec)
# #
# # #
# # def asciiToStr(dec):
# #     """"""
# #     return chr(dec)
# #
# #
# # #
# # def paramsInput():
# #     params = input('请输入：')
# #     print('to Ascii:{0}'.format(strToAscii(params)))
# #     print('to Str:{0}'.format(asciiToStr(strToAscii(params))))
# #     paramsInput()
# #
# #
# # #
# # if __name__ == '__main__':
# #     paramsInput()
#
#
# # TODO;Python 最大公约数算法
# #
# # # 定义一个函数
# # def hcf(x, y):
# #     """该函数返回两个数的最大公约数"""
# #
# #     # 获取最小值
# #     if x > y:
# #         smaller = y
# #     else:
# #         smaller = x
# #
# #     for i in range(1, smaller + 1):
# #         if (x % i == 0) and (y % i == 0):
# #             hcf = i
# #
# #     return hcf
# #
# #
# # # 用户输入两个数字
# # num1 = int(input("输入第一个数字: "))
# # num2 = int(input("输入第二个数字: "))
# #
# # print(num1, "和", num2, "的最大公约数为", hcf(num1, num2))
#
#
# # TODO;Python 最小公倍数算法
# #
# #
# # # 定义函数
# # def lcm(x, y):
# #     #  获取最大的数
# #     if x > y:
# #         greater = x
# #     else:
# #         greater = y
# #
# #     while (True):
# #         if (greater % x == 0) and (greater % y == 0):
# #             lcm = greater
# #             break
# #         greater += 1
# #
# #     return lcm
# #
# #
# # # 获取用户输入
# # num1 = int(input("输入第一个数字: "))
# # num2 = int(input("输入第二个数字: "))
# #
# # print(num1, "和", num2, "的最小公倍数为", lcm(num1, num2))
#
#
# # TODO;Python 简单计算器实现
# #
# # # 以下代码用于实现简单计算器实现，包括两个数基本的加减乘除运输：
# #
# # # 定义函数
# # def add(x, y):
# #     """相加"""
# #
# #     return x + y
# #
# #
# # def subtract(x, y):
# #     """相减"""
# #
# #     return x - y
# #
# #
# # def multiply(x, y):
# #     """相乘"""
# #
# #     return x * y
# #
# #
# # def divide(x, y):
# #     """相除"""
# #
# #     return x / y
# #
# #
# # def paramsInput():
# #     """"""
# #
# #     # 用户输入
# #     print("选择运算：")
# #     print("1、相加")
# #     print("2、相减")
# #     print("3、相乘")
# #     print("4、相除")
# #
# #     choice = input("输入你的选择(1/2/3/4):")
# #
# #     num1 = int(input("输入第一个数字: "))
# #     num2 = int(input("输入第二个数字: "))
# #
# #     if choice == '1':
# #         print(num1, "+", num2, "=", add(num1, num2))
# #
# #     elif choice == '2':
# #         print(num1, "-", num2, "=", subtract(num1, num2))
# #
# #     elif choice == '3':
# #         print(num1, "*", num2, "=", multiply(num1, num2))
# #
# #     elif choice == '4':
# #         print(num1, "/", num2, "=", divide(num1, num2))
# #     else:
# #         print("非法输入")
# #
# #
# # if __name__ == '__main__':
# #     while True:
# #         print('\n')
# #         paramsInput()
# #         print('\n')
# #
#
# # TODO;Python 生成日历
# #
# # import calendar
# #
# #
# # def generCalander(yy, mm):
# #     """"""
# #     return calendar.month(yy, mm)
# #
# #
# # def paramsInput():
# #     """"""
# #     yy = int(input('请输入年份：'))
# #     mm = int(input('请输入月份：'))
# #
# #     print(generCalander(yy, mm))
# #     paramsInput()
# #
# #
# # if __name__ == '__main__':
# #     paramsInput()
#
#
# # TODO;Python 使用递归斐波那契数列
# #
# #
# # def recur_fibo(n):
# #     """递归函数
# #     输出斐波那契数列"""
# #     if n <= 1:
# #         return n
# #     else:
# #         return (recur_fibo(n - 1) + recur_fibo(n - 2))
# #
# #
# # # 获取用户输入
# # nterms = int(input("您要输出几项? "))
# #
# # # 检查输入的数字是否正确
# # if nterms <= 0:
# #     print("输入正数")
# # else:
# #     print("斐波那契数列:")
# #     for i in range(nterms):
# #         print(recur_fibo(i))
# #
# #
#
# # TODO;Python 文件 IO
# #
# # # 写文件
# # with open("test.txt", "wt") as out_file:
# #     out_file.write("该文本会写入到文件中\n看到我了吧！")
# #
# # # Read a file
# # with open("test.txt", "rt") as in_file:
# #     text = in_file.read()
# #
# # print(text)
#
#
# # TODO;Python 字符串判断
# #
# #
# # # 测试实例一
# # print("测试实例一")
# # str = "runoob.com"
# # print(str.isalnum())  # 判断所有字符都是数字或者字母
# # print(str.isalpha())  # 判断所有字符都是字母
# # print(str.isdigit())  # 判断所有字符都是数字
# # print(str.islower())  # 判断所有字符都是小写
# # print(str.isupper())  # 判断所有字符都是大写
# # print(str.istitle())  # 判断所有单词都是首字母大写，像标题
# # print(str.isspace())  # 判断所有字符都是空白字符、\t、\n、\r
# #
# # print("------------------------")
# #
# # # 测试实例二
# # print("测试实例二")
# # str = "runoob"
# # print(str.isalnum())
# # print(str.isalpha())
# # print(str.isdigit())
# # print(str.islower())
# # print(str.isupper())
# # print(str.istitle())
# # print(str.isspace())
#
#
# # TODO;Python 字符串大小写转换
# #
# # ssstr = "I am look at tv ."
# # print(ssstr.upper())  # 把所有字符中的小写字母转换成大写字母
# # print(ssstr.lower())  # 把所有字符中的大写字母转换成小写字母
# # print(ssstr.capitalize())  # 把第一个字母转化为大写字母，其余小写
# # print(ssstr.title())  # 把每个单词的第一个字母转化为大写，其余小写
# #
# #
# #
#
#
# # TODO;Python 计算每个月天数
# #
# # import calendar
# #
# #
# # def generMonthDay(yy, mm):
# #     """"""
# #     return calendar.monthrange(yy, mm)
# #
# #
# # def paramsInput():
# #     """"""
# #     yy = int(input('输入年份：'))
# #     mm = int(input('输入月份：'))
# #
# #     print(generMonthDay(yy, mm))
# #     paramsInput()
# #
# #
# # if __name__ == '__main__':
# #     paramsInput()
# #
# # # 输出的是一个元组，第一个元素是所查月份的第一天对应的是星期几（0-6），
# # # 第二个元素是这个月的天数。
# # # 以上实例输出的意思为 2016 年 9 月份的第一天是星期四，该月总共有 30 天。
# #
# #
# #
#
# # TODO;Python 获取昨天日期
#
# # import datetime
# #
# #
# # def getYesterday():
# #     """"""
# #     today = datetime.date.today()
# #     oneday = datetime.timedelta(days=1)
# #     return today - oneday
# #
# #
# # if __name__ == '__main__':
# #     print('昨天是：{0}'.format(getYesterday()))
#
# # TODO;Python list 常用操作
#
# # 1.1.list 定义
# from os.path import join
#
# li = ['aaa', 'bb', 'cc', 'dd']
# print('li :{li}'.format(li=li))
# print('li[1]:{0}'.format(li[1]))
#
#
# # 2.list 负数索引
#
# print('li[-1] :{0}'.format(li[-1] ))
#
#
#
# # 3.list 增加元素
#
# li.append("new")
# print('li :{li}'.format(li=li))
#
# li.insert(2, "new")
# print('li :{li}'.format(li=li))
#
# li.extend(["two", "elements"])
# print('li :{li}'.format(li=li))
#
#
# # 4.list 搜索
#
#
# print('index \'new\' in li is :{0}'.format(li.index('new')))
# print('index \'dd\' in li is :{0}'.format(li.index('dd')))
# # print('index \'ee\' in li is :{0}'.format(li.index('ee')))
#
#
# # 5.list 删除元素
#
# li.insert(0,'z')
# print('li :{li}'.format(li=li))
# li.remove("z")
# print('li :{li}'.format(li=li))
#
# li.pop()
# print('li :{li}'.format(li=li))
# li.pop()
# print('li :{li}'.format(li=li))
#
#
# # 6.list 运算符
#
# li = li + ['example', 'new']
# print('li :{li}'.format(li=li))
#
# li += [1, 2] * 3
# print('li :{li}'.format(li=li))
#
#
# # 7.使用join链接list成为字符串
#
# params = {"server": "mpilgrim", "database": "master", "uid": "sa", "pwd": "secret"}
# print(";".join(["%s=%s" % (k, v) for k, v in params.items()]))
# # join 只能用于元素是字符串的 list; 它不进行任何的类型强制转换。连接一个存在一个或多个非字符串元素的 list 将引发一个异常。
#
# # 8.list 分割字符串
#
# li = ['server=mpilgrim', 'uid=sa', 'database=master', 'pwd=secret']
#
# s = ";".join(li)
#
# print(s)
#
# print(s.split(";"))
#
# print(s.split(";", 1) )
#
# # split 与 join 正好相反, 它将一个字符串分割成多元素 list。
# # 注意, 分隔符 (";") 被完全去掉了, 它没有在返回的 list 中的任意元素中出现。
# # split 接受一个可选的第二个参数, 它是要分割的次数。
#
#
# # 9.list 的映射解析
# li = [1, 9, 8, 4]
#
# print([elem*2 for elem in li])
#
# li = [elem*2 for elem in li]
# print(li  )
#
#
#
# # 10.dictionary中的解析
#
# params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
# print('keys:',params.keys())
# print('values:',params.values())
# print('items:',params.items())
#
# print([k for k, v in params.items()])
# print([v for k, v in params.items()])
# print(["%s=%s" % (k, v) for k, v in params.items()])
#
#
#
#
# # 11.list 过滤
# li = ["a", "mpilgrim", "foo", "b", "c", "b", "d", "d"]
#
# print( [elem for elem in li if len(elem) > 1])
#
# print([elem for elem in li if elem != "b"])
#
# print([elem for elem in li if li.count(elem) == 1])
#
