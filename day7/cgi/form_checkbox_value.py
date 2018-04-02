# TODO;通过CGI程序传递checkbox数据

# 引入 CGI 处理模块
import cgi, cgitb

# 创建 FieldStorage的实例
form = cgi.FieldStorage()

# 接收字段数据
if form.getvalue('google'):
    google_flag = "是"
else:
    google_flag = "否"

if form.getvalue('runoob'):
    runoob_flag = "是"
else:
    runoob_flag = "否"

print("Content-type:text/html")
print()
print("<html>")
print("<head>")
print("<meta charset=\"utf-8\">")
print("<title>菜鸟教程 CGI 测试实例</title>")
print("</head>")
print("<body>")
print("<h2> 菜鸟教程是否选择了 : %s</h2>" % runoob_flag)
print("<h2> Google 是否选择了 : %s</h2>" % google_flag)
print("</body>")
print("</html>")

# cp ./day7/cgi/form_checkbox_value.py /Users/wangxiaolong/Downloads/Download/apache-tomcat-9.0.6/webapps/ROOT/WEB-INF/cgi/form_checkbox_value.py
