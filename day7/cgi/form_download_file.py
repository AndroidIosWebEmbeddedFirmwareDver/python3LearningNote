# TODO;文件下载对话框

"""
我们先在当前目录下创建 foo.txt 文件，用于程序的下载。

文件下载通过设置HTTP头信息来实现，功能代码如下：

"""

# HTTP 头部
print("Content-Disposition: attachment; filename=\"form_download_file.py\"")
print()
# 打开文件
fo = open("form_download_file.py", "r")

str = fo.read();
print(str)

# 关闭文件
fo.close()


# cp ./day7/cgi/form_download_file.py /Users/wangxiaolong/Downloads/Download/apache-tomcat-9.0.6/webapps/ROOT/WEB-INF/cgi/form_download_file.py

