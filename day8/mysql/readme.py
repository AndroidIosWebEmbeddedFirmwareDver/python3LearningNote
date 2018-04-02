
# TODO;Python3 MySQL 数据库连接
"""
本文我们为大家介绍 Python3 使用 PyMySQL 连接数据库，并实现简单的增删改查。

什么是 PyMySQL？
PyMySQL 是在 Python3.x 版本中用于连接 MySQL 服务器的一个库，Python2中则使用mysqldb。

PyMySQL 遵循 Python 数据库 API v2.0 规范，并包含了 pure-Python MySQL 客户端库。
"""
# TODO;PyMySQL 安装

"""
在使用 PyMySQL 之前，我们需要确保 PyMySQL 已安装。

PyMySQL 下载地址：https://github.com/PyMySQL/PyMySQL。

如果还未安装，我们可以使用以下命令安装最新版的 PyMySQL：

$ pip install PyMySQL
如果你的系统不支持 pip 命令，可以使用以下方式安装：

1、使用 git 命令下载安装包安装(你也可以手动下载)：

$ git clone https://github.com/PyMySQL/PyMySQL
$ cd PyMySQL/
$ python3 setup.py install
2、如果需要制定版本号，可以使用 curl 命令来安装：

$ # X.X 为 PyMySQL 的版本号
$ curl -L https://github.com/PyMySQL/PyMySQL/tarball/pymysql-X.X | tar xz
$ cd PyMySQL*
$ python3 setup.py install
$ # 现在你可以删除 PyMySQL* 目录
注意：请确保您有root权限来安装上述模块。

安装的过程中可能会出现"ImportError: No module named setuptools"的错误提示，

意思是你没有安装setuptools，你可以访问https://pypi.python.org/pypi/setuptools 找到各个系统的安装方法。

Linux 系统安装实例：

$ wget https://bootstrap.pypa.io/ez_setup.py
$ python3 ez_setup.py

"""

