#!/usr/bin/env python3
#coding: utf-8
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender = 's'
receiver = 'zengjc@163.com'
subject = 'python email test'
smtpserver = '192.168.9.112'
username = 's'
password = 's' 

msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = 'test message' 

msgText = MIMEText('这是邮件正文内容',_subtype='plain',_charset='gb2312')
msgRoot.attach(msgText)

#构造附件
att = MIMEText(open('E:\\python\\parameter.ini', 'r').read(), 'base64', 'utf-8')
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = 'attachment; filename="parameter.ini"'
msgRoot.attach(att) 

smtp = smtplib.SMTP()
smtp.connect('192.168.9.112')
smtp.login(username, password)
smtp.sendmail(sender, receiver, msgRoot.as_string())
smtp.quit()