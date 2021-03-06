# Python3 解释器

# TODO;2018年01月23日16:56:31


"""

Linux/Unix的系统上，一般默认的 python 版本为 2.x，我们可以将 python3.x 安装在 /usr/local/python3 目录中。

安装完成后，我们可以将路径 /usr/local/python3/bin 添加到您的 Linux/Unix 操作系统的环境变量中，
~~~
$ PATH=$PATH:/usr/local/python3/bin/python3    # 设置环境变量
$ python3 --version
Python 3.4.0
~~~
这样您就可以通过 shell 终端输入下面的命令来启动 Python3 。


在Window系统下你可以通过以下命令来设置Python的环境变量，假设你的Python安装在 C:\Python34 下:
~~~
set path=%path%;C:\python34
~~~

"""


# 交互式编程


"""
我们可以在命令提示符中输入"Python"命令来启动Python解释器：
~~~
$ python3
~~~

执行以上命令后，出现如下窗口信息：
~~~
$ python3
Python 3.4.0 (default, Apr 11 2014, 13:05:11) 
[GCC 4.8.2] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 

~~~
在 python 提示符中输入以下语句，然后按回车键查看运行效果：

~~~
print ("Hello, Python!");
~~~

以上命令执行结果如下：

~~~
Hello, Python!
~~~


当键入一个多行结构时，续行是必须的。我们可以看下如下 if 语句：

~~~

>>> flag = True
>>> if flag :
...     print("flag 条件为 True!")
... 
flag 条件为 True!

~~~


"""

# 脚本式编程

"""

将如下代码拷贝至 hello.py文件中：

~~~
print ("Hello, Python!");
~~~
通过以下命令执行该脚本：

~~~
python3 hello.py
~~~

输出结果为：
~~~
Hello, Python!
~~~

在Linux/Unix系统中，你可以在脚本顶部添加以下命令让Python脚本可以像SHELL脚本一样可直接执行：

~~~
#! /usr/bin/env python3
~~~
然后修改脚本权限，使其有执行权限，命令如下：
~~~
$ chmod +x hello.py
~~~

执行以下命令：
~~~
./hello.py
~~~

输出结果为：
~~~
Hello, Python!
~~~

"""
