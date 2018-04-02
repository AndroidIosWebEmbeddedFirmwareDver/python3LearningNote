# TODO;GET和POST方法
"""
浏览器客户端通过两种方法向服务器传递信息，这两种方法就是 GET 方法和 POST 方法。

使用GET方法传输数据
GET方法发送编码后的用户信息到服务端，数据信息包含在请求页面的URL上，以"?"号分割, 如下所示：

http://www.test.com/cgi-bin/hello.py?key1=value1&key2=value2 有关 GET 请求的其他一些注释：
GET 请求可被缓存
GET 请求保留在浏览器历史记录中
GET 请求可被收藏为书签
GET 请求不应在处理敏感数据时使用
GET 请求有长度限制
GET 请求只应当用于取回数据
简单的url实例：GET方法
以下是一个简单的URL，使用GET方法向hello_get.py程序发送两个参数：

/cgi-bin/test.py?name=菜鸟教程&url=http://www.runoob.com
以下为hello_get.py文件的代码：

"""

# CGI处理模块
import cgi, cgitb

# 创建 FieldStorage 的实例化
form = cgi.FieldStorage()

# 获取数据
site_name = form.getvalue('name')
site_url = form.getvalue('url')

print("Content-type:text/html")
print()
print("<html>")
print("<head>")
print("<meta charset=\"utf-8\">")
print("<title>菜鸟教程 CGI 测试实例</title>")
print("</head>")
print("<body>")
print("<h2>%s官网：%s</h2>" % (site_name, site_url))
print("</body>")
print("</html>")

# http://localhost:8080/cgi-bin/hello_get.py?name=sss&url=www.sss.org
