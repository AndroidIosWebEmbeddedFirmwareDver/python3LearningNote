# TODO;什么是时间元组？

"""
很多Python函数用一个元组装起来的9组数字处理时间:
序号	字段	        值
----------------------------------------------------
0	4位数年	    2008
1	月	        1 到 12
2	日	        1到31
3	小时	        0到23
4	分钟	        0到59
5	秒	        0到61 (60或61 是闰秒)
6	一周的第几日	0到6 (0是周一)
7	一年的第几日	1到366 (儒略历)
8	夏令时	    -1, 0, 1, -1是决定是否为夏令时的旗帜
----------------------------------------------------

"""

"""
上述也就是struct_time元组。这种结构具有如下属性：

序号	属性	        值
----------------------------------------------------
0	tm_year	    2008
1	tm_mon	    1 到 12
2	tm_mday 	1 到 31
3	tm_hour	    0 到 23
4	tm_min	    0 到 59
5	tm_sec	    0 到 61 (60或61 是闰秒)
6	tm_wday	    0到6 (0是周一)
7	tm_yday	    一年中的第几天，1 到 366
8	tm_isdst	是否为夏令时，值有：1(夏令时)、0(不是夏令时)、-1(未知)，默认 -1
----------------------------------------------------
"""
"""
NamedTuple(
            '_struct_time',
            [('tm_year', int), ('tm_mon', int), ('tm_mday', int),
             ('tm_hour', int), ('tm_min', int), ('tm_sec', int),
             ('tm_wday', int), ('tm_yday', int), ('tm_isdst', int),
             ('tm_zone', str), ('tm_gmtoff', int)]
        )
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
