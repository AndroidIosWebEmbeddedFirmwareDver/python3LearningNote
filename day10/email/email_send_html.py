# TODO;使用Python发送HTML格式的邮件


"""
Python发送HTML格式的邮件与发送纯文本消息的邮件不同之处就是将MIMEText中_subtype设置为html。具体代码如下：
"""

import smtplib
from email.mime.text import MIMEText
from email.header import Header


def done():
    try:
        sender = 'wondershealth@wondersgroup.com'
        receivers = ['wangxiaolong@wondersgroup.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

        mail_msg = """
        <p>Python 邮件发送测试...</p>
        <p><a href="http://www.baidu.com">这是一个链接</a></p>
        """
        message = MIMEText(mail_msg, 'html', 'utf-8')
        message['From'] = Header("天天打豆豆", 'utf-8')
        message['To'] = Header("测试", 'utf-8')

        subject = 'Python SMTP 邮件测试'
        message['Subject'] = Header(subject, 'utf-8')

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
        print('-->>%s' % x)
        done()


"""
执行以上程序，如果你本机安装sendmail，就会输出：

$ python3 test.py 
邮件发送成功
查看我们的收件箱(一般在垃圾箱)，就可以查看到邮件信息：

"""


