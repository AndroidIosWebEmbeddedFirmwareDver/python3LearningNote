# TODO;获取格式化的时间
"""
你可以根据需求选取各种格式，但是最简单的获取可读的时间模式的函数是asctime():
"""

import time

formatLoaclTime = time.asctime(time.localtime(time.time()))

print('本地时间：', formatLoaclTime)

# TOOD;格式化日期

"""
我们可以使用 time 模块的 strftime 方法来格式化日期，：

time.strftime(format[, t])

"""
FORMAT_TEMPLE_1 = '%Y-%m-%d %H:%M:%S'
FORMAT_TEMPLE_2 = '%a %b %d %H:%M:%S %Y'

print(time.strftime(FORMAT_TEMPLE_1, time.localtime()))
print(time.strftime(FORMAT_TEMPLE_2, time.localtime()))

# 将格式字符串转换为时间戳
print(time.mktime(time.strptime(time.strftime(FORMAT_TEMPLE_2, time.localtime()), FORMAT_TEMPLE_2)))

"""
python中时间日期格式化符号：
---------------------------------------
%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12）
%M 分钟数（00=59）
%S 秒（00-59）
%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称
%% %号本身
---------------------------------------
"""
