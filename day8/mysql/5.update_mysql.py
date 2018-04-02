# TODO;数据库更新操作
"""
更新操作用于更新数据表的的数据，以下实例将 TESTDB表中的 SEX 字段全部修改为 'M'，AGE 字段递增1：
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

    # SQL 更新语句
    sql = "UPDATE {0} SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M').format(table_name)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except Exception as e:
        # 发生错误时回滚
        db.rollback()
        print(e)

    # 关闭数据库连接
    db.close()


if __name__ == '__main__':
    done()
