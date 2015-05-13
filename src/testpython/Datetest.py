# -*- coding: UTF-8 -*-

# 获取今天、昨天和明天的日期
# 引入datetime模块
#import datetime
import datetime
import time
#计算今天的时间
today = datetime.date.today()
#计算昨天的时间  
yesterday = today - datetime.timedelta(days = 1)
#计算明天的时间 
tomorrow = today + datetime.timedelta(days = 1)  
#打印这三个时间
print(yesterday, today, tomorrow)
#trailtime=datetime.strptime('', '%Y-%m-%d %H:%M:%S')

trailfiletimeStr = '2015-04-15 12:00:05'
trailfiletime = datetime.datetime.strptime(trailfiletimeStr, '%Y-%m-%d %H:%M:%S')

print(type(trailfiletime))
#print(time.strptime('%Y-%m-%d %H:%M:%S',trailfiletime))
if trailfiletime <= (datetime.datetime.now() - datetime.timedelta(days=1)):
    print('一天前更新的')
print(trailfiletime)
i=0
while i<=3:
     print (i)
     i=i+1
     
timenow = datetime.datetime.now()
timedelay = timenow + datetime.timedelta(seconds=3)
time.sleep(2)
if datetime.datetime.now() >= timedelay :
    print ('时间已过，可以干活')
else:
    print ('频率太高！')