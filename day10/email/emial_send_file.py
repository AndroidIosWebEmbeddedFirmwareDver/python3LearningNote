# TODO;Python 发送带附件的邮件
"""
发送带附件的邮件，首先要创建MIMEMultipart()实例，然后构造附件，如果有多个附件，可依次构造，最后利用smtplib.smtp发送。
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header


def done():
    try:
        sender = 'wondershealth@wondersgroup.com'
        receivers = ['wangxiaolong@wondersgroup.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

        # 创建一个带附件的实例
        message = MIMEMultipart()
        message['From'] = Header("天天玩PP", 'utf-8')
        message['To'] = Header("测试", 'utf-8')
        subject = 'Python SMTP 邮件测试'
        message['Subject'] = Header(subject, 'utf-8')

        # 邮件正文内容
        message.attach(MIMEText('这是天天玩PPPython 邮件发送测试……', 'plain', 'utf-8'))

        # 构造附件1，传送当前目录下的  文件
        att1 = MIMEText(open('test.txt', 'rb').read(), 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        att1["Content-Disposition"] = 'attachment; filename="test.txt"'
        message.attach(att1)

        # 构造附件2，传送当前目录下的 文件
        att2 = MIMEText(open('email_send_demo.py', 'rb').read(), 'base64', 'utf-8')
        att2["Content-Type"] = 'application/octet-stream'
        att2["Content-Disposition"] = 'attachment; filename="email_send_demo.py"'
        message.attach(att2)

        # 构造附件3，传送当前目录下的 文件
        att3 = MIMEText(open('email_send_html.py', 'rb').read(), 'base64', 'utf-8')
        att3["Content-Type"] = 'application/octet-stream'
        att3["Content-Disposition"] = 'attachment; filename="email_send_html.py"'
        message.attach(att3)

        try:
            smtpObj = smtplib.SMTP('smtp.wondersgroup.com')
            smtpObj.sendmail(sender, receivers, message.as_string())
            print("邮件发送成功")
        except smtplib.SMTPException:
            print("Error: 无法发送邮件")
    except Exception as e:
        print(e)


if __name__ == '__main__':
    for x in range(0, 10):
        print('emial with MIMEMultipart -->>{0}'.format(x))
        done()
