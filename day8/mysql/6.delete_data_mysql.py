# TODO;删除操作
"""
删除操作用于删除数据表中的数据，以下实例演示了删除数据表 EMPLOYEE 中 AGE 大于 20 的所有数据：
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

    # SQL 删除语句
    sql = "DELETE FROM {0} WHERE AGE > '%d'".format(table_name) % (19)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交修改
        db.commit()
    except Exception as e:
        # 发生错误时回滚
        db.rollback()
        print(e)

    # 关闭连接
    db.close()


if __name__ == '__main__':
    done()
