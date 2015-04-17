# -*- coding: utf-8 -*-
'''
本程序通过putty工具下载linux/AIX文件，需要提供以下内容：
putty工具：psftp
linux/AIX用户名、密码
'''  
import os
import log
import datetime
#命令行，包含了登录IP、账户信息、batchcmd.txt存放psftp中运行的命令
#batchcmd.txt主要 包含了更换下载文件存放路径、下载文件等
cmdStr='psftp.exe root@192.168.127.21 -pw shcic123 -b batchcmd.txt'
#日志存放路径
logpath='E:\\python\\log\\testpython.log'
#存放putty的psftp工具的本地路径
localPath='E:\\python\\installfile\\putty'


def getFile(cmdStr):
    log.writeLog('传输FTP日志：开始',logpath)
    os.chdir(localPath)
    os.system(cmdStr)
    log.writeLog('传输FTP日志：结束',logpath)
    
def checkOGGLogfile(filepath):
    #定义trail文件分割符，从下列行中解析出最后收到的trail文件序号和接收时间
    #Opened trail file /usr/oracle/ggs/dirdat/rep_in/realestate/aa000428 at 2011-12-12 11:42:21
    trail_split='aa000'
    trail_file_number=0 #trail文件序号
    trail_file_time='' #trail文件读取时间
    
    #
    #读取文件
    try: 
        with open(filepath,encoding='UTF-8') as sourcefile:
            #line_number=0 
            for a_line in sourcefile: 
                #line_number += 1
                if 'Opened trail file' in a_line:
                    #print('{:>4}{}'.format(line_number,a_line.rstrip()))
                    #根据
                    trail_file_number=a_line[a_line.index(trail_split)+len(trail_split):a_line.index(' at ')]
                    trail_file_time=a_line[a_line.index(' at ')+4:-1]
    except:
        log.writeLog(filepath+'文件不存在啊，赶快处理啊！',logpath)
        raise ValueError(filepath+'文件不存在啊，赶快处理啊！')
    
    #解析文件，判断最后接收时间是否在可接受范围内
    try:
        #if trail_file_number = 0 :
        #   pass 
        today = datetime.datetime.now()
        trail_file_time = datetime.datetime.strptime(trail_file_time, '%Y-%m-%d %H:%M:%S')
        if trail_file_time <= (today - datetime.timedelta(days=1)):
            log.writeLog('最后文件序号：'+str(trail_file_number)+' 最后更新时间：' +str(trail_file_time) + '一天前更新的，有问题！！！')
            return 1 #有问题，需处理
        else:
            return 0 #没问题

    except:
        log.writeLog('解析文件出错',logpath)
        raise ValueError('解析文件出错')
        


if __name__ == '__main__':
    #getFile(cmdStr)
    filepath='E:\\python\\R_I_AA.rpt'
    checkOGGLogfile(filepath)