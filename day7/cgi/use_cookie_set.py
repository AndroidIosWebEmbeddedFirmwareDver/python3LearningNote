# TODO;CGI中使用Cookie
# """
# 在 http 协议一个很大的缺点就是不对用户身份的进行判断，这样给编程人员带来很大的不便，
# 而 cookie 功能的出现弥补了这个不足。
#
# cookie 就是在客户访问脚本的同时，通过客户的浏览器，在客户硬盘上写入纪录数据 ，当下
# 次客户访问脚本时取回数据信息，从而达到身份判别的功能，cookie 常用在身份校验中。
#
# """
#
# """
# cookie的语法
# http cookie的发送是通过http头部来实现的，他早于文件的传递，头部set-cookie的语法如下：
#
# Set-cookie:name=name;expires=date;path=path;domain=domain;secure
#
# name=name: 需要设置cookie的值(name不能使用";"和","号),有多个name值时用 ";" 分隔，
#             例如：name1=name1;name2=name2;name3=name3。
# expires=date: cookie的有效期限,格式： expires="Wdy,DD-Mon-YYYY HH:MM:SS"
# path=path: 设置cookie支持的路径,如果path是一个路径，则cookie对这个目录下的所有文件
#             及子目录生效，例如： path="/cgi-bin/"，如果path是一个文件，则cookie指对这个文件生
#             效，例如：path="/cgi-bin/cookie.cgi"。
# domain=domain: 对cookie生效的域名，例如：domain="www.runoob.com"
# secure: 如果给出此标志，表示cookie只能通过SSL协议的https服务器来传递。
# cookie的接收是通过设置环境变量HTTP_COOKIE来实现的，CGI程序可以通过检索该变量获取cookie信息。
#
# """

# TODO;Cookie设置
"""
Cookie的设置非常简单，cookie会在http头部单独发送。以下实例在cookie中设置了name 和 expires：
"""

print('Content-Type: text/html')
print('Set-Cookie: name="142356778183416asd12357167238dawe12367";expires=Wed, 28 Aug 2022 18:30:00 GMT')
print()
print("""
<html>
  <head>
    <meta charset="utf-8">
    <title>sssssss</title>
  </head>
    <body>
        <h1>Cookie set OK!</h1>
    </body>
</html>
""")

"""
将以上代码保存到 cookie_set.py，并修改 cookie_set.py 权限：

chmod 755 cookie_set.py
以上实例使用了 Set-Cookie 头信息来设置Cookie信息，可选项中设置了Cookie的其他属性，如过期时间Expires，域名Domain，
路径Path。这些信息设置在 "Content-type:text/html"之前。
"""

# cp ./day7/cgi/use_cookie_set.py /Users/wangxiaolong/Downloads/Download/apache-tomcat-9.0.6/webapps/ROOT/WEB-INF/cgi/use_cookie_set.py
