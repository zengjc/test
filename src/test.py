# -*- coding: UTF-8 -*-
import os
fileo=open("E:\\python\\结果.xls")
try:
    textdata=fileo.read()
finally:
    fileo.close()

fileout=open("E:\\python\\结果-修改后.xls",'w')
fileout.write(textdata.replace('charset=UTF-8','charset=GBK'))
fileout.close()
print(type(textdata))
logname='n2'
if logname == 'n':
    logname=os.getcwd()+'\\log.log'
else:
    logname=logname
print(logname)    
