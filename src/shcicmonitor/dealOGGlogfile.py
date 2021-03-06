# -*- coding: utf-8 -*-
'''
本程序通过putty工具下载linux/AIX文件，需要提供以下内容：
putty工具：psftp
linux/AIX用户名、密码
modify at 2015-12-21
增加对ogg日志检查过程的容错
'''  
import os
import datetime
import tools

def downloadfile(cmdstr):
    '''
            传入下载命令，通过putty工具进行下载
    '''
    tools.writeLog('传输FTP日志：开始')
    # 更改本地目录到psftp工具的路径
    localpath = tools.readconfig('dealOGGlog', 'localPath')
    os.chdir(localpath)
    # 下载
    os.system(cmdstr)
    tools.writeLog('传输FTP日志：结束')
    
def checkOGGLogfile(trailfiletime, delaydays):
    '''
    delaydays为最大延迟天数，当超过该天数后，认定时间失败
            根据trail最后处理时间进行判断：0-正常 ， 1-异常
    '''
    # 解析文件，判断最后接收时间是否在可接受范围内
    #
    legalday = datetime.datetime.now() - datetime.timedelta(days=delaydays)
    try:
        trailfiletime = datetime.datetime.strptime(trailfiletime, '%Y-%m-%d %H:%M:%S')
    except:
        tools.writeLog('检查文件过程异常，检查结果：异常！')
        return 1  # 异常，需处理
    
    if trailfiletime <= legalday:
        tools.writeLog('检查文件完成，检查结果：异常！')
        return 1  # 异常，需处理
    else:
        tools.writeLog('检查文件完成，检查结果：正常！')
        return 0  # 没问题
        
def splitOGGlog(filepath, splitstr, splitstrtime=' at '):
    '''
             传入OGG日志文件路径和分隔符，解析出trail最后序列号和最后文件读取时间
    '''
    trailfilenumber = None  # trail文件序号
    trailfiletime = None  # trail文件读取时间
    # 读取文件
    try: 
        with open(filepath, encoding='UTF-8') as sourcefile:
            # line_number=0 
            for a_line in sourcefile: 
                # line_number += 1
                if 'Opened trail file' in a_line:
                    # print('{:>4}{}'.format(line_number,a_line.rstrip()))
                    trailfilenumber = a_line[a_line.index(splitstr) + len(splitstr):a_line.index(' at ')]
                    trailfiletime = a_line[a_line.index(' at ') + 4:-1]
    except:
        tools.writeLog(filepath + '文件不存在啊，赶快处理啊！')
#         raise ValueError(filepath + '文件不存在啊，赶快处理啊！')
    #不报错，而是返回错误代码
        return 0000,'OGG日志文件异常'
    tools.writeLog('最后文件序号：' + str(trailfilenumber) + ' 最后更新时间：' + str(trailfiletime))
    
    return trailfilenumber, trailfiletime

def getcheckOGGr_i_ba(delaydays):
    '''
            监控R_I_BA进程
            返回值：result：0-正常；1-异常 ；
    '''
    cmdstr = tools.readconfig('dealOGGlog', 'cmdStr')
    downloadfile(cmdstr)
    
    trialsplit = tools.readconfig('dealOGGlog', 'trailsplit')
    trailfilepath = tools.readconfig('dealOGGlog', 'trailfilepath')
    trailfile = splitOGGlog(trailfilepath, trialsplit)
    result = checkOGGLogfile(trailfile[1], delaydays)
    return result, trailfile[1]
    
    
if __name__ == '__main__':
    getcheckOGGr_i_ba(1)
    
