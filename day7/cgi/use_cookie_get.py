# TODO;CGI中使用Cookie


# TODO;检索Cookie信息
"""
Cookie信息检索页非常简单，Cookie信息存储在CGI的环境变量HTTP_COOKIE中，存储格式如下：

key1=value1;key2=value2;key3=value3....

以下是一个简单的CGI检索cookie信息的程序：
"""

# 导入模块
import os
import http.cookies
from http.cookiejar import Cookie

print("Content-type: text/html")
print()

print("""
<html>
<head>
<meta charset="utf-8">
<title>222222</title>
</head>
<body>
<h1>读取cookie信息</h1>
""")

if 'HTTP_COOKIE' in os.environ:
    cookie_string = os.environ.get('HTTP_COOKIE')
    c = Cookie.SimpleCookie()
    c.load(cookie_string)

    try:
        data = c['name'].value
        print("cookie data: " + data + "<br>")
    except KeyError:
        print("cookie 没有设置或者已过去<br>")
print("""
</body>
</html>
""")

# cp ./day7/cgi/use_cookie_get.py /Users/wangxiaolong/Downloads/Download/apache-tomcat-9.0.6/webapps/ROOT/WEB-INF/cgi/use_cookie_get.py
