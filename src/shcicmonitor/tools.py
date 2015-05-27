# -*- coding: UTF-8 -*-
'''
Created on 2015年4月20日

@author: zjc
'''
import configparser
import time
import os
configpath = 'E:\\python\\eclipse\\workspace\\testpython\\src\\shcicmonitor\\parameter.ini'

def readconfig(field, key):
    cf = configparser.ConfigParser()
    # 必须指定字符集，否则容易出错
    cf.read(configpath, encoding='utf-8')
    result = ''
    try:
        result = cf.get(field, key)
    except:
        result = ''  
    return result  
  
def writeLog(logdata):
    #
    logpath = readconfig('log', 'logpath')    
    # print(logpath)
    try:
        with open(logpath, mode='a', encoding='UTF-8') as logfile:
            date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            logfile.write(date + ' : ' + logdata + '\n')
    except:
        raise('日志文件不存在或无法打开！！')

def nowtime():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

if __name__ == "__main__":
    writeLog('日志测试！')
    print (readconfig('log', 'logpath'))
    print (nowtime())
