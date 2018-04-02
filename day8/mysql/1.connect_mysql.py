# TODO;数据库连接
"""
连接数据库前，请先确认以下事项：

您已经创建了数据库 TESTDB.
在TESTDB数据库中您已经创建了表 EMPLOYEE
EMPLOYEE表字段为 FIRST_NAME, LAST_NAME, AGE, SEX 和 INCOME。
连接数据库TESTDB使用的用户名为 "testuser" ，密码为 "test123",你可以可以自
己设定或者直接使用root用户名及其密码，Mysql数据库用户授权请使用Grant命令。
在你的机子上已经安装了 Python MySQLdb 模块。
如果您对sql语句不熟悉，可以访问我们的 SQL基础教程
实例：
以下实例链接 Mysql 的 TESTDB 数据库：
"""

import pymysql

if __name__ == '__main__':

    try:
        # 打开数据库，返回数据库实例
        db = pymysql.connect('localhost', 'root', 'admin2018', 'yitaodesign')
        # 获取游标
        cursor = db.cursor()

        # 使用 execute()  方法执行 SQL 查询
        cursor.execute('SELECT VERSION()')

        # 使用 fetchone() 方法获取单条数据.
        data = cursor.fetchone()
        print(data)
        print("Database version : %s " % data)

        # 使用 execute()  方法执行 SQL 查询
        cursor.execute('SHOW DATABASES;')
        # 使用 fetchall() 方法获取所有数据.
        for database in cursor.fetchall():
            print("DataBase %s 's tables:" % database)
            print('--' * 20)
            cursor = db.cursor()
            print('USE %s ;' % database)
            cursor.execute('USE %s ;' % database)
            cursor.execute('SHOW TABLES FROM  %s ;' % database)
            for table in cursor.fetchall():
                print(" %s " % table)
                try:
                    print('--' * 20)
                    cursor = db.cursor()
                    # cursor.execute('USE %s ;' % database)
                    print('SELECT * FROM  %s ;' % table)
                    cursor.execute('SELECT * FROM  %s ;' % table)
                    for row in cursor.fetchall():
                        # print("<br> %s," % row)
                        print(row)
                        print('%s' * len(row) % row)
                        # print('---.....')
                except Exception as e:
                    print(e)
            print('--' * 20)

        # 关闭数据库连接
        db.close()
    except Exception as e:
        print(e)
