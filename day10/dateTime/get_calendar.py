#
#
# TODO;获取某月日历
"""
Calendar模块有很广泛的方法用来处理年历和月历，例如打印某月的月历：
"""

import calendar

# year = 2019
# month = 9

if __name__ == '__main__':
    inputTimes = 0
    while True:
        year = int(input('输入年份（1970~2999）：'))
        month = int(input('输入月份（1~12）：'))
        inputTimes += 1
        cal = calendar.month(year, month)
        # print("{0}年{1}日历".format(year, month))
        # print('-' * 20)
        # print(cal)
        # print('-' * 20)

        print("{0}\n{1}年{2}日历\n{3}\n{4}\n{5}".format('-' * 20, year, month, '-' * 20, cal, '-' * 20))

        if inputTimes == 3:
            exit()
