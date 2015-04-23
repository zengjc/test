# -*- coding: UTF-8 -*-
'''
Created on 2015年4月21日
发送邮件，可包含附件
@author: zjc
'''
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import tools
import time


def sendmail(maildata):
    sender = tools.readconfig('mail', 'sender')
    receiver = tools.readconfig('mail', 'receiver')
    subject = tools.readconfig('mail', 'subject')
    smtpserver = tools.readconfig('mail', 'smtpserver')
    username = tools.readconfig('mail', 'username')
    password = tools.readconfig('mail', 'password')
    attachfile = tools.readconfig('mail', 'attachfile')

    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = subject 
    
    date = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    msgText = MIMEText(date + maildata,_subtype='plain',_charset='gb2312')
    msgRoot.attach(msgText)
    
    #构造附件
    if attachfile != '':
        att = MIMEText(open(attachfile, 'rb').read(), 'base64', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = 'attachment; filename="parameter.ini"'
        msgRoot.attach(att)
    
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msgRoot.as_string())
    smtp.quit()
    tools.writeLog('邮件已发送给：'+receiver)
    
if __name__ == '__main__':  
    maildata='邮件测试！！sendmail.py'
    sendmail(maildata)
