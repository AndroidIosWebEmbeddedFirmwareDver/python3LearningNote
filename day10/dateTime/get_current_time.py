# TODO;获取当前时间

"""
从返回浮点数的时间辍方式向时间元组转换，只要将浮点数传递给如localtime之类的函数。
"""

import time

currentLocaltime = time.localtime(time.time())
print('本地时间为：{0}'.format(currentLocaltime))

print('年:', currentLocaltime.tm_year)
print('月:', currentLocaltime.tm_mon)
print('日:', currentLocaltime.tm_mday)
print('时:', currentLocaltime.tm_hour)
print('分:', currentLocaltime.tm_min)
print('秒:', currentLocaltime.tm_sec)
print('星期:', currentLocaltime.tm_wday)
print('今年第{0}天'.format(currentLocaltime.tm_yday))

if currentLocaltime.tm_isdst == 1:
    print('夏令时')
elif currentLocaltime.tm_isdst == 0:
    print('非夏令时')
else:
    print('未知')
