# -*- coding: UTF-8 -*-
import os

import datetime 

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

#today = datetime.today()
#print(today)
#print(datetime.strptime('2011-12-12 14:00:01', '%Y-%m-%d %H:%M:%S')+datetime.timedelta(days=1))
#starttime = datetime.strptime('2015-04-12 14:00:01', '%Y-%m-%d %H:%M:%S')
#long running
endtime = datetime.datetime.now()
#print (endtime - starttime).seconds

#today = datetime.date.today()
#yesterday = today - datetime.timedelta(days=1)

today = datetime.date.today()
yesterday = today - datetime.timedelta(days = 1)  
tomorrow = today + datetime.timedelta(days = 1) 
print(yesterday, today, tomorrow)

str='   abcde '
print(len(str))
pathname='E:\\python\\R_I_AA.rpt'
print(os.path.split(pathname)[1])