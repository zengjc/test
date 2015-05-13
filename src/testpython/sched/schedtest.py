import time, sched

#被调度触发的函数
def event_func(msg):
    print("Current Time:", time.strftime("%y-%m-%d %H:%M:%S"), 'msg:', msg)

def run_function():
    #初始化sched模块的scheduler类
    s = sched.scheduler(time.time, time.sleep)
    #设置一个调度,因为time.sleep()的时间是一秒,所以timer的间隔时间就是sleep的时间,加上enter的第一个参数
    s.enter(0, 2, event_func, ("Timer event.",))
    s.run()

def timer1():
    while True:
        #sched模块不是循环的，一次调度被执行后就Over了，如果想再执行，可以使用while循环的方式不停的调用该方法
        time.sleep(1)
        run_function()

if __name__ == "__main__":
    timer1()