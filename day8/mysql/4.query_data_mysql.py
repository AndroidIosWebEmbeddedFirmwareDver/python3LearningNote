# TODO;数据库查询操作

"""
Python查询Mysql使用 fetchone() 方法获取单条数据, 使用fetchall() 方法获取多条数据。

fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
fetchall(): 接收全部的返回结果行.
rowcount: 这是一个只读属性，并返回执行execute()方法后影响的行数。
实例：
查询EMPLOYEE表中salary（工资）字段大于1000的所有数据：

"""

import pymysql

#
table_name = 'A_TEST_TABLE_BY_PYTHON'


def done():
    """"""
    # 打开数据库，返回数据库实例
    db = pymysql.connect('localhost', 'root', 'admin2018', 'yitaodesign')

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 查询语句
    sql = "SELECT * FROM {0} \
           WHERE INCOME > '%d'".format(table_name) % (1000)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            fname = row[0]
            lname = row[1]
            age = row[2]
            sex = row[3]
            income = row[4]
            # 打印结果
            print("fname=%s,lname=%s,age=%s,sex=%s,income=%s" % \
                  (fname, lname, age, sex, income))
    except Exception as e:
        print("Error: unable to fetch data")
        print(e)

    # 关闭数据库连接
    db.close()


if __name__ == '__main__':
    done()
