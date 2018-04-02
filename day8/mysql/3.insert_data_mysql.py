# TODO;数据库插入操作

"""
以下实例使用执行 SQL INSERT 语句向表 EMPLOYEE 插入记录
"""
import pymysql

#
table_name = 'A_TEST_TABLE_BY_PYTHON'


def done():
    """"""
    # 打开数据库，返回数据库实例
    db = pymysql.connect('localhost', 'root', 'admin2018', 'yitaodesign')
    # 获取游标
    cursor = db.cursor()

    # SQL 插入语句
    sql = """INSERT INTO {0}(FIRST_NAME,
             LAST_NAME, AGE, SEX, INCOME)
             VALUES ('Mac', 'Mohan', 20, 'M', 2000)""".format(table_name)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except Exception as e:
        # 如果发生错误则回滚
        db.rollback()
        print(e)
    # 关闭数据库连接
    db.close()


def done2():
    """"""
    # 打开数据库，返回数据库实例
    db = pymysql.connect('localhost', 'root', 'admin2018', 'yitaodesign')
    # 获取游标
    cursor = db.cursor()

    # SQL 插入语句
    sql = "INSERT INTO {0}(FIRST_NAME, \
           LAST_NAME, AGE, SEX, INCOME) \
           VALUES ('%s', '%s', '%d', '%c', '%d' )".format(table_name) % \
          ('Mac', 'Mohan', 20, 'M', 2000)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 执行sql语句
        db.commit()
    except Exception as e:
        # 发生错误时回滚
        db.rollback()
        print(e)

    # 关闭数据库连接
    db.close()


if __name__ == '__main__':
    for x in range(0,100):
        done()
        done2()
