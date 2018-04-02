# # TODO;Python CGI编程
# #
# # """
# # CGI 目前由NCSA维护，NCSA定义CGI如下：
# #
# # CGI(Common Gateway Interface),通用网关接口,它是一段程序,运行在服务器上如：HTTP服务器，提供同客户端HTML页面的接口。
# #
# # """
# #
# # # TODO;网页浏览
# #
# # """
# # 为了更好的了解CGI是如何工作的，我们可以从在网页上点击一个链接或URL的流程：
# #
# # 1、使用你的浏览器访问URL并连接到HTTP web 服务器。
# # 2、Web服务器接收到请求信息后会解析URL，并查找访问的文件在服务器上是否存在，如果存在返回文件的内容，否则返回错误信息。
# # 3、浏览器从服务器上接收信息，并显示接收的文件或者错误信息。
# # CGI程序可以是Python脚本，PERL脚本，SHELL脚本，C或者C++程序等。
# #
# # http://www.runoob.com/wp-content/uploads/2013/11/Cgi01.png
# # """
# # # TODO;CGI架构图
# # """
# # day7/Cgi01.png
# # """
# #
# # # TODO;Web服务器支持及配置
# #
# # """
# # 在你进行CGI编程前，确保您的Web服务器支持CGI及已经配置了CGI的处理程序。
# #
# # Apache 支持CGI 配置：
# #
# # 设置好CGI目录：
# #
# # ScriptAlias /cgi-bin/ /var/www/cgi-bin/
# # 所有的HTTP服务器执行CGI程序都保存在一个预先配置的目录。这个目录被称为CGI目录，并按照惯例，它被命名为/var/www/cgi-bin目录。
# #
# # CGI文件的扩展名为.cgi，python也可以使用.py扩展名。
# #
# # 默认情况下，Linux服务器配置运行的cgi-bin目录中为/var/www。
# #
# # 如果你想指定其他运行CGI脚本的目录，可以修改httpd.conf配置文件，如下所示：
# #
# # <Directory "/var/www/cgi-bin">
# #    AllowOverride None
# #    Options +ExecCGI
# #    Order allow,deny
# #    Allow from all
# # </Directory>
# # 在 AddHandler 中添加 .py 后缀，这样我们就可以访问 .py 结尾的 python 脚本文件：
# #
# # AddHandler cgi-script .cgi .pl .py
# # """
# #
# # """
# # MAC TOMCAT
# #
# # cgi 路径：/Users/wangxiaolong/Downloads/Download/apache-tomcat-9.0.6/webapps/ROOT/WEB-INF/cgi
# # 指令：cp ./day7/t3_cgi.py /Users/wangxiaolong/Downloads/Download/apache-tomcat-9.0.6/webapps/ROOT/WEB-INF/cgi/t3_cgi.py
# # 访问路径：http://localhost:8080/cgi-bin/t3_cgi.py
# # """
# # #
# # filename: test1.cgi
#
#
#
# print("Content-type: text/html\n\n");
# #print("Hello, world!\n");
# #print("Hello, world!\n");
# #print("Hello, world!\n");
# #print("Hello, world!\n\n");
# #print("Hello, world!\n");
# #print '<br>\n\nhhh';
# #print '<html>';
# #print '<head>';
# #print '</head>';
# #print '<body>';
# #print '<h1>adad</h1>';
# #print '<h2>adad</h2>';
# #print '<h3>adad</h3>';
# #print '<h4>adad</h4>';
# #print '<h5>adad</h5>';
# #print '</body>';
# #print '</html>';
# print('<html>');
# print('<head>');
# print('<meta charset="utf-8">');
# print('</head>');
# print('<body>');
# print('<h1>Hello Word - 我的第一个 CGI 程序！</h1>');
# print('<h2>Hello Word - 我的第一个 CGI 程序！</h2>');
# print('<h3>Hello Word - 我的第一个 CGI 程序！</h3>');
# print('<h4>Hello Word - 我的第一个 CGI 程序！</h4>');
# print('<h5>Hello Word - 我的第一个 CGI 程序！</h5>');
# print('</body>');
# print('</html>');
#
#
#
#
#
# """
# 这个的hello.py脚本是一个简单的Python脚本，脚本第一行的输出内容"Content-type:text/html"发送到浏览器并告知浏览器显示的内容类型为"text/html"。
#
# 用 print 输出一个空行用于告诉服务器结束头部信息。
#
# HTTP头部
# hello.py文件内容中的" Content-type:text/html"即为HTTP头部的一部分，它会发送给浏览器告诉浏览器文件的内容类型。
#
# HTTP头部的格式如下：
#
# HTTP 字段名: 字段内容
# 例如：
#
# Content-type: text/html
# 以下表格介绍了CGI程序中HTTP头部经常使用的信息：
#
# 头	描述
# Content-type:	请求的与实体对应的MIME信息。例如: Content-type:text/html
# Expires: Date	响应过期的日期和时间
# Location: URL	用来重定向接收方到非请求URL的位置来完成请求或标识新的资源
# Last-modified: Date	请求资源的最后修改时间
# Content-length: N	请求的内容长度
# Set-Cookie: String	设置Http Cookie
#
# CGI环境变量
# 所有的CGI程序都接收以下的环境变量，这些变量在CGI程序中发挥了重要的作用：
#
# 变量名	描述
# CONTENT_TYPE	这个环境变量的值指示所传递来的信息的MIME类型。目前，环境变量CONTENT_TYPE一般都是：
#                 application/x-www-form-urlencoded,他表示数据来自于HTML表单。
# CONTENT_LENGTH	如果服务器与CGI程序信息的传递方式是POST，这个环境变量即使从标准输入STDIN中可以读
#                 到的有效数据的字节数。这个环境变量在读取所输入的数据时必须使用。
# HTTP_COOKIE	    客户机内的 COOKIE 内容。
# HTTP_USER_AGENT	提供包含了版本数或其他专有数据的客户浏览器信息。
# PATH_INFO	    这个环境变量的值表示紧接在CGI程序名之后的其他路径信息。它常常作为CGI程序的参数出现。
# QUERY_STRING	如果服务器与CGI程序信息的传递方式是GET，这个环境变量的值即使所传递的信息。这个信息经
#                 跟在CGI程序名的后面，两者中间用一个问号'?'分隔。
# REMOTE_ADDR	    这个环境变量的值是发送请求的客户机的IP地址，例如上面的192.168.1.67。这个值总是存在的。
#                 而且它是Web客户机需要提供给Web服务器的唯一标识，可以在CGI程序中用它来区分不同的Web客户机。
# REMOTE_HOST	    这个环境变量的值包含发送CGI请求的客户机的主机名。如果不支持你想查询，则无需定义此环境变量。
# REQUEST_METHOD	提供脚本被调用的方法。对于使用 HTTP/1.0 协议的脚本，仅 GET 和 POST 有意义。
# SCRIPT_FILENAME	CGI脚本的完整路径
# SCRIPT_NAME	    CGI脚本的的名称
# SERVER_NAME	    这是你的 WEB 服务器的主机名、别名或IP地址。
# SERVER_SOFTWARE	这个环境变量的值包含了调用CGI程序的HTTP服务器的名称和版本号。例如，上面的值为Apache/2
#                 .2.14(Unix)
#
# 以下是一个简单的CGI脚本输出CGI的环境变量：
#
# """
#
# import os
#
# print("Content-type: text/html");
# print('<html>');
# print('<head>');
# print('<meta charset="utf-8">');
# print('</head>');
# print('<body>');
# print('<h1>adasdad</h1>');
# print("<b>环境变量</b><br>");
# print("<ul>");
# for key in os.environ.keys():
#     print("<li><span style='color:green'>%30s </span> : %s </li>" % (key, os.environ[key]));
# print("</ul>");
# print('</body>');
# print('</html>');
#
# TODO；MAC本地Apache
# sudo apachectl stop
# sudo apachectl restart
# /usr/local/var/www/cgi-bin
# """
# DocumentRoot is /usr/local/var/www.
#
# The default ports have been set in /usr/local/etc/httpd/httpd.conf to 8080 and in
# /usr/local/etc/httpd/extra/httpd-ssl.conf to 8443 so that httpd can run without sudo.
#
# To have launchd start httpd now and restart at login:
#   brew services start httpd
# Or, if you don't want/need a background service you can just run:
#   apachectl start
#
# """
#
# TODO;CGI文件目录： /Users/wangxiaolong/Downloads/Download/apache-tomcat-9.0.6/webapps/ROOT/WEB-INF/cgi/
# TODO;浏览访问路径：http://localhost:8080/cgi-bin/hello.py


# !/usr/bin/python3

print("Content-type:text/html")
print()  # 空行，告诉服务器结束头部
print('<html>')
print('<head>')
print('<meta charset="utf-8">')
print('<title>Hello Word - 我的第一个 CGI 程序！</title>')
print('</head>')
print('<body>')
print('<h2>Hello Word! <br>我是第一CGI程序</h2>')
print('</body>')
print('</html>')
