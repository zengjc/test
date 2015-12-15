# -*- coding: UTF-8 -*-

# 获取今天、昨天和明天的日期
# 引入datetime模块
def testdatetime():
    from datetime import datetime
    # 计算今天的时间
    today = datetime.date.today()
    # 计算昨天的时间  
    yesterday = today - datetime.timedelta(days=1)
    # 计算明天的时间 
    tomorrow = today + datetime.timedelta(days=1)  
    # 打印这三个时间
    print(yesterday, today, tomorrow)
    # trailtime=datetime.strptime('', '%Y-%m-%d %H:%M:%S')
    
    trailfiletimeStr = '2015-04-15 12:00:05'
    trailfiletime = datetime.datetime.strptime(trailfiletimeStr, '%Y-%m-%d %H:%M:%S')
    
    print(type(trailfiletime))
    if trailfiletime <= (datetime.datetime.now() - datetime.timedelta(days=1)):
        print('一天前更新的')
    print(trailfiletime)
    i = 0
    while i <= 3:
         print (i)
         i = i + 1
         
    # timenow = datetime.datetime.now()
    # timedelay = timenow + datetime.timedelta(seconds=3)
    # time.sleep(2)
    # if datetime.datetime.now() >= timedelay :
    #     print ('时间已过，可以干活')
    # else:
    #     print ('频率太高！')

def testtime():
    import time
    timestr = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time()))
    print (timestr)
    constr = '* 12 * *'  # 分 时 日  月
    timenow = time.strftime('%M %H %d %m %Y', time.localtime(time.time())).split(sep=' ')
    i = 0
    for con in constr.split(sep=' '):
        if con != '*':
            timenow[i] = con
            print (con)
        i += 1
    print (timenow)
    time1 = ''
    i = 0
    for con in timenow:
        time1 = time1 + timenow[i] + ' '
        i += 1
    print (time1)
    print (time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(time1.rstrip(), '%M %H %d %m %Y')))
    if time.localtime(time.time()) > time.strptime(time1.rstrip(), '%M %H %d %m %Y'):
        print ('吉时已到！')
        timestr
    
def testdatetime2(schedulestr):
    from datetime import datetime
    # 将时间拆分成元组，并用定时器中配置替换相对应的时间
    scheduletuple = datetime.today().strftime("%M %H %d %m %Y").split(sep=' ')
    i = 0
    delay = 0
    delaydict = {0:3600,1:86400,2:1036800,3:1036800}
    for element in schedulestr.split(sep=' '):
        if element != '*':
            scheduletuple[i] = element
            if delay == 0 :
                delay = delaydict[i]
        i += 1
    print (scheduletuple)
    # 把元组组合成字符串，并转换为时间
    scheduletime = ''
    i = 0
    for element in scheduletuple:
        scheduletime = scheduletime + scheduletuple[i] + ' '
        i += 1
    # 判断是否是良辰吉日
    if datetime.now() >= datetime.strptime(scheduletime.rstrip(), '%M %H %d %m %Y'):
        print ('吉时已到！出发！')
    else:
        print ('等待！')
    #返回系统需要延时的时间
    return delay

def testdatetime3():
    from datetime import datetime
    yearno = 2013
    print (datetime.today().replace(year=yearno))
    
if __name__ == '__main__':
    print (testdatetime2('* 12 * *'))
    print (testdatetime2('2 12 * 7'))
    print (testdatetime2('1 * * 7'))
