# TODO;python使用SAX解析xml


"""
SAX是一种基于事件驱动的API。

利用SAX解析XML文档牵涉到两个部分:解析器和事件处理器。

解析器负责读取XML文档,并向事件处理器发送事件,如元素开始跟元素结束事件;

而事件处理器则负责对事件作出相应,对传递的XML数据进行处理。

1、对大型文件进行处理；
2、只需要文件的部分内容，或者只需从文件中得到特定信息。
3、想建立自己的对象模型的时候。
在python中使用sax方式处理xml要先引入xml.sax中的parse函数，还有xml.sax.handler中的ContentHandler。

"""

# TODO;ContentHandler类方法介绍
"""
characters(content)方法

    调用时机：
    
    从行开始，遇到标签之前，存在字符，content的值为这些字符串。
    
    从一个标签，遇到下一个标签之前， 存在字符，content的值为这些字符串。
    
    从一个标签，遇到行结束符之前，存在字符，content的值为这些字符串。
    
    标签可以是开始标签，也可以是结束标签。

startDocument()方法

    文档启动的时候调用。

endDocument()方法

    解析器到达文档结尾时调用。

startElement(name, attrs)方法

    遇到XML开始标签时调用，name是标签的名字，attrs是标签的属性值字典。

endElement(name)方法

遇   到XML结束标签时调用。
"""

# TODO;make_parser方法
"""
以下方法创建一个新的解析器对象并返回。
    xml.sax.make_parser( [parser_list] )
参数说明:
    parser_list - 可选参数，解析器列表
"""

# TODO;parser方法
"""
以下方法创建一个 SAX 解析器并解析xml文档：
    xml.sax.parse( xmlfile, contenthandler[, errorhandler])
参数说明:
    xmlfile - xml文件名
    contenthandler - 必须是一个ContentHandler的对象
    errorhandler - 如果指定该参数，errorhandler必须是一个SAX ErrorHandler对象
"""

# TODO;parseString方法
"""
parseString方法创建一个XML解析器并解析xml字符串：
    xml.sax.parseString(xmlstring, contenthandler[, errorhandler])
参数说明:
    xmlstring - xml字符串
    contenthandler - 必须是一个ContentHandler的对象
    errorhandler - 如果指定该参数，errorhandler必须是一个SAX ErrorHandler对象
"""

# TODO;Python 解析XML实例

import xml.sax


class CommonHandler(xml.sax.ContentHandler):
    def __init__(self):
        """"""

    def startDocument(self):
        """收到文档开头的通知。"""

    def endDocument(self):
        """收到文件结尾的通知。"""

    def startPrefixMapping(self, prefix, uri):
        """开始前缀URI命名空间映射的范围。"""

    def endPrefixMapping(self, prefix):
        """结束前缀URI映射的范围。"""

    def startElement(self, name, attrs):
        """在非命名空间模式下指示元素的开始。"""

    def endElement(self, name):
        """在非命名空间模式下指示元素的结尾。"""

    def startElementNS(self, name, qname, attrs):
        """在命名空间模式中指示元素的开始。"""

    def endElementNS(self, name, qname):
        """在命名空间模式中指示元素的结尾。"""

    def characters(self, content):
        """接收字符数据通知。"""

    def ignorableWhitespace(self, whitespace):
        """收到可忽略空白元素内容的通知。"""

    def processingInstruction(self, target, data):
        """接收处理指令的通知。"""

    def skippedEntity(self, name):
        """接收跳过实体的通知。"""


class SimpleHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.tag = ""
        self.content = ""

    # 元素开始调用
    def startElement(self, tag, attributes):
        self.tag = tag

    # 元素结束调用
    def endElement(self, tag):
        print('{0}:{1}'.format(self.tag, self.content))
        self.content = ""

    # 读取字符时调用
    def characters(self, content):
        self.content = content


class MovieHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.type = ""
        self.format = ""
        self.year = ""
        self.rating = ""
        self.stars = ""
        self.description = ""

    # 元素开始调用
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "movie":
            print("*****Movie*****")
            title = attributes["title"]
            print("Title:", title)

    # 元素结束调用
    def endElement(self, tag):
        if self.CurrentData == "type":
            print("Type:", self.type)
        elif self.CurrentData == "format":
            print("Format:", self.format)
        elif self.CurrentData == "year":
            print("Year:", self.year)
        elif self.CurrentData == "rating":
            print("Rating:", self.rating)
        elif self.CurrentData == "stars":
            print("Stars:", self.stars)
        elif self.CurrentData == "description":
            print("Description:", self.description)
        self.CurrentData = ""

    # 读取字符时调用
    def characters(self, content):
        if self.CurrentData == "type":
            self.type = content
        elif self.CurrentData == "format":
            self.format = content
        elif self.CurrentData == "year":
            self.year = content
        elif self.CurrentData == "rating":
            self.rating = content
        elif self.CurrentData == "stars":
            self.stars = content
        elif self.CurrentData == "description":
            self.description = content


if __name__ == '__main__':
    # 创建一个 XMLReader
    parser = xml.sax.make_parser()
    # turn off namepsaces
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # 重写 ContextHandler
    handler = MovieHandler()
    parser.setContentHandler(handler)

    parser.parse("movies.xml")

    #
    # # 重写 ContextHandler
    # handler = SimpleHandler()
    # parser.setContentHandler(handler)
    #
    # parser.parse("movies.xml")

# https://docs.python.org/3/library/xml.sax.html
