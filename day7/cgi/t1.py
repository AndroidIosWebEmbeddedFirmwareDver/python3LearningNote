# TODO;HTTP头部
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
