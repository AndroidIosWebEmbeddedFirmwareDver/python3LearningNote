# TODO;在 HTML 文本中添加图片

"""
邮件的 HTML 文本中一般邮件服务商添加外链是无效的，正确添加突破的实例如下所示：
"""

import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header


def done():
    """"""
    try:

        sender = 'wondershealth@wondersgroup.com'
        receivers = ['wangxiaolong@wondersgroup.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

        msgRoot = MIMEMultipart('related')
        msgRoot['From'] = Header("天天玩OO", 'utf-8')
        msgRoot['To'] = Header("测试", 'utf-8')
        subject = 'Python SMTP 邮件测试'
        msgRoot['Subject'] = Header(subject, 'utf-8')

        msgAlternative = MIMEMultipart('alternative')
        msgRoot.attach(msgAlternative)

        mail_msg = """
        <p>Python 邮件发送测试...</p>
        <p><a href="http://www.baidu.com">天天玩OO链接</a></p>
        <p>图片演示：</p>
        <p><img src="cid:image1"></p>
        """
        msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))

        # 指定图片为当前目录
        fp = open('test.png', 'rb')
        msgImage = MIMEImage(fp.read())
        fp.close()

        # 定义图片 ID，在 HTML 文本中引用
        msgImage.add_header('Content-ID', '<image1>')
        msgRoot.attach(msgImage)

        try:
            smtpObj = smtplib.SMTP('smtp.wondersgroup.com')
            smtpObj.sendmail(sender, receivers, msgRoot.as_string())
            print("邮件发送成功")
        except smtplib.SMTPException:
            print("Error: 无法发送邮件")
    except Exception as e:
        print(e)


if __name__ == '__main__':
    for x in range(0, 10):
        print('email with image-->%s' % x)
        done()


"""
$ python3 test.py 
邮件发送成功
查看我们的收件箱(如果在垃圾箱可能需要移动到收件箱才可正常显示)，就可以查看到邮件信息：



更多内容请参阅：https://docs.python.org/3/library/email-examples.html。

"""