# -*- coding: UTF-8 -*-
'''
Created on 2015年4月20日
由外网操作系统调度，每天运行一次
@author: zjc
'''
import dealOGGlogfile
import config
import string
#
delaydays = config.readconfig('dealOGGlog', 'delaydays_r_i_ba')
dealOGGlogfile.getcheckOGGr_i_ba(int(delaydays))
