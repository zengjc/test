# -*- coding: UTF-8 -*-
'''
Created on 2015年4月20日

@author: zjc
'''
import configparser
configpath='E:\\python\\parameter.ini'
  
def readconfig(field, key):
    cf = configparser.ConfigParser()  
    cf.read(configpath)
    result=''
    try:
        result = cf.get(field, key)
    except:
        result=''  
    return result  
  
  
if __name__ == "__main__":
    print (readconfig('log','logpath'))
