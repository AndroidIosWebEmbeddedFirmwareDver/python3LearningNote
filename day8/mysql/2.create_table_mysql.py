# TODO;创建数据库表


"""
如果数据库连接存在我们可以使用execute()方法来为数据库创建表，如下所示创建表EMPLOYEE：
"""
# 打开数据库连接
import pymysql


def done():
    """"""
    try:
        # 打开数据库，返回数据库实例
        db = pymysql.connect('localhost', 'root', 'admin2018', 'yitaodesign')
        # 获取游标
        cursor = db.cursor()

        table_name = 'A_TEST_TABLE_BY_PYTHON'

        # 使用 execute() 方法执行 SQL，如果表存在则删除
        cursor.execute("DROP TABLE IF EXISTS {0}".format(table_name))

        # 使用预处理语句创建表
        sql = """CREATE TABLE {0} (
                 FIRST_NAME  CHAR(20) NOT NULL,
                 LAST_NAME  CHAR(20),
                 AGE INT,
                 SEX CHAR(1),
                 INCOME FLOAT )""".format(table_name)

        cursor.execute(sql)

        # 关闭数据库连接
        db.close()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    done()
