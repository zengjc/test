# -*- coding: UTF-8 -*-
'''
写日志函数，输入：日志内容
Created on 2015-04-07

@author: zjc
'''
import time
import os

filename='E:\\python\\log\\testpython.log'

def writeLog(filedata):
    try:
        with open(filename,mode='a',encoding='UTF-8') as logfile:
            date = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            logfile.write(date + ' : ' + filedata + '\n')
    except:
        raise('日志文件不存在或无法打开！！')