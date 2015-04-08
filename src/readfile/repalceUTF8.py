# -*- coding: UTF-8 -*-

'''
Created on 2015-3-27

@author: zjc
'''
import time
from readfile import log
#time.sleep(2)
log.writeLog(filedata='替换文件开始！')
try: 
    with open('E:\\python\\结果.xls',encoding='GBK') as sourcefile:
        sourcedata=sourcefile.read()
except:
    log.writeLog('文件不存在啊，赶快处理啊！')
    raise ValueError('文件不存在啊，赶快处理啊！')

with open('E:\\python\\结果_替换后.xls','w') as targetfile:
     log.writeLog('开始重写文件！')
     targetfile.write(sourcedata.replace('charset=UTF-8','charset=GBK'))    

log.writeLog('替换文件顺利结束！')


