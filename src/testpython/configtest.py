# -*- coding: utf-8 -*-
'''
Created on 2015年4月20日

@author: zjc
'''
import configparser
 
config = configparser.ConfigParser()
config.read('E:\\python\\parameter.ini')

print (config.sections())
print (config.get("log","logpath"))
print (config['dealOGGlog'])
print (config['dealOGGlog']['trail_split'])
