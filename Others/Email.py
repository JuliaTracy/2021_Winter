# -*- coding: UTF-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = '你的QQ邮箱'
receivers = ['你想发的邮箱']

message = MIMEText('邮件内容', 'plain', 'utf-8')
message['From'] = Header("抬头", 'utf-8')
message['To'] = Header("你的落款", 'utf-8')

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

smtpObj = smtplib.SMTP_SSL("smtp.qq.com", 465)
smtpObj.login(sender, "")  #需注册一个协议
smtpObj.sendmail(sender, receivers, message.as_string())
smtpObj.quit()
print("邮件发送成功")
