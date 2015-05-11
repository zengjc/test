# -*- coding: utf-8 -*-
'''
Created on 2015年4月20日

@author: zjc
'''
import configparser
from shcicmonitor import tools
import os
 
config = configparser.ConfigParser()
config.read('E:\\python\\parameter.ini')

print (config.sections())
print (config.get("log","logpath"))
print (config['dealOGGlog'])


file=tools.readconfig('mail', 'attachfile')
print(file)
print(os.path.split(file)[1])

str='''系统运行状态：[系统运行结果]
-------------------------------------
1.外网OGG状态：[状态1]
最后处理时间：[trial时间]

-------------------------------------'''
print (str)
str=str.replace('[系统运行结果]', '系统运行正常')
str=str.replace('[状态1]', 'OGG运行正常')

print (str)




