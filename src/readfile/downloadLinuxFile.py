# -*- coding: utf-8 -*-  
import os
import log
#存放putty的psftp工具的本地路径
localPath='E:\\python\\installfile\\putty'
#命令行，包含了登录IP、账户信息、batchcmd.txt存放psftp中运行的命令
#batchcmd.txt主要 包含了更换下载文件存放路径、下载文件等
cmdStr='psftp.exe root@192.168.127.21 -pw shcic123 -b batchcmd.txt'
#日志存放路径
logpath='E:\\python\\log\\testpython.log'

log.writeLog('传输FTP日志：开始',logpath)
os.chdir(localPath)
os.system(cmdStr)
log.writeLog('传输FTP日志：结束',logpath)
