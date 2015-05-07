# -*- coding: UTF-8 -*-
'''
发送txt文本邮件
小五义：http://www.cnblogs.com/xiaowuyi
'''
import smtplib  
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

mailto_list=["zengjc@163.com","11607150@qq.com"] 
mail_host="192.168.9.112"  #设置服务器
mail_user="s"    #用户名
mail_pass="s"   #口令 
mail_postfix="shcic.com"  #发件箱的后缀
  
def send_mail(to_list,sub,content):  
    msgRoot = MIMEMultipart('related')
    #msgRoot['Subject'] = file_name#邮件标题，这里我把标题设成了你所发的附件名
    msgText = MIMEText('%s'%content,'html','utf-8')#你所发的文字信息将以html形式呈现
    msgRoot.attach(msgText)

    
    me="hello"+"<"+mail_user+"@"+mail_postfix+">"  
    msg = MIMEText(content,_subtype='plain',_charset='gb2312')  
    msg['Subject'] = sub  
    msg['From'] = me  
    msg['To'] = ";".join(to_list)
    
    
    
    try:  
        server = smtplib.SMTP()  
        server.connect(mail_host)  
        server.login(mail_user,mail_pass)  
        server.sendmail(me, to_list, msg.as_string())  
        server.close()  
        return True  
    except :  
        #print str(e)  
        return False  
if __name__ == '__main__':  
    date = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    if send_mail(mailto_list,"hello","hello world！"+date):  
        print ("发送成功")  
    else:  
        print ("发送失败")