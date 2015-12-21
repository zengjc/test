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
modify on 20151221
增加OGG日志检查过程的容错处理
@author: zjc
'''
import dealOGGlogfile
import tools
import sendmail
import dealgapfile
#
def dojobww():
    # 邮件正文模板
    maildata = '''系统运行状态：
[系统运行结果]
--------------------------
1.外网房源标注同步：
[状态1]
OGG最后处理时间：
[trial时间]

2.外网网闸：[网闸状态2]
最后同步时间：[网闸同步时间2]
--------------------------
最后检查时间：
[检查时间]'''
    tools.writeLog('----------外网监控任务：开始！----------')
    
    #1 检查外网房源标注OGG运行状态
    delaydays = tools.readconfig('dealOGGlog', 'delaydays_r_i_ba')
    oggresult = dealOGGlogfile.getcheckOGGr_i_ba(int(delaydays))
    
    #2 检查外网网闸工作状态
    gappathww = tools.readconfig('gap', 'shuiwu_nankang_gap_path')
    gapdaysww = tools.readconfig('gap', 'shuiwu_nankang_gap_time')
    gapresultww = dealgapfile.checkgap(gappathww, int(gapdaysww))
    
    # 根据监控结果，编写邮件正文内容
    #1 外网OGG状态
    if oggresult[0] == 0:
        maildata = maildata.replace('[状态1]', '正常')
        maildata = maildata.replace('[trial时间]', oggresult[1])
    else:
        maildata = maildata.replace('[状态1]', '异常')
        maildata = maildata.replace('[trial时间]', '异常')
    #2 外网网闸
    if gapresultww[0] == 0:
        maildata = maildata.replace('[网闸状态2]', '正常')
        maildata = maildata.replace('[网闸同步时间2]', gapresultww[1])
    elif gapresultww[0] == 1:
        maildata = maildata.replace('[网闸状态2]', '异常')
        maildata = maildata.replace('[网闸同步时间2]', gapresultww[1])
    else:
        maildata = maildata.replace('[网闸状态2]', '异常')
        maildata = maildata.replace('[网闸同步时间2]', '未找到数据')
    
    # 系统整体运行状态
    if oggresult[0] == 0 and gapresultww[0] == 0:
        maildata = maildata.replace('[系统运行结果]', '全部正常！')
    else:
        maildata = maildata.replace('[系统运行结果]', '发生异常！')
    
    maildata = maildata.replace('[检查时间]', tools.nowtime())
    
    tools.writeLog('外网监控结果：\n' + maildata)
    tools.writeLog('----------外网监控任务：结束！----------')
    return maildata

if __name__ == '__main__':
    checkresult = dojobww()
    sendmail.sendmail(checkresult)