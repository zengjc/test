# -*- coding: UTF-8 -*-
'''
Created on 2015年4月20日
由外网操作系统调度，每天运行一次
邮件正文模板：
系统运行状态：正常/异常
-------------------------------------
1.外网OGG状态：正常/异常
最后处理时间：


-------------------------------------
@author: zjc
'''
import dealOGGlogfile
import tools
import sendmail
#邮件正文模板


#
def dojobww():
    maildata='''系统运行状态：[系统运行结果]
    -------------------------------------
    1.外网OGG状态：[状态1]
    最后处理时间：[trial时间]
    
    -------------------------------------'''
    tools.writeLog('----------外网监控任务：开始！----------')
    delaydays = tools.readconfig('dealOGGlog', 'delaydays_r_i_ba')
    oggresult=dealOGGlogfile.getcheckOGGr_i_ba(int(delaydays))
    maildata=maildata.replace('[trial时间]', oggresult[1])
    
    #根据监控结果，编写邮件正文内容--外网OGG状态
    if oggresult[0] == 0:
        maildata=maildata.replace('[状态1]', 'OGG运行正常')
    else:
        maildata=maildata.replace('[状态1]', 'OGG运行异常')
    
    if oggresult[0] == 0:
        maildata=maildata.replace('[系统运行结果]', '系统运行正常！')
    else:
        maildata=maildata.replace('[系统运行结果]', '系统运行异常！')
    
    tools.writeLog('----------外网监控任务：结束！----------')
    return maildata

if __name__ == '__main__':
    checkresult=dojobww()
    sendmail.sendmail(checkresult)

