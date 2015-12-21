# -*- coding: UTF-8 -*-
'''
Created on 2015年5月26日

@author: zjc
'''
import os
import datetime
from shcicmonitor import tools
def getfolderlastmtime(folderpath):
    '''
    获取文件夹中最后修改的文件名称和时间，用于网闸同步监控，不检查子文件夹
    返回值：文件名称 string , 最后修改时间 datetime
    '''
    filelastmtime = None
    filelastmname = None
    fileflag = 0 #初始化标志
    #如果不是文件夹，立刻返回
    if not os.path.isdir(folderpath):
        return filelastmname,filelastmtime,fileflag
    #遍历文件
    for filename in os.listdir(path=folderpath):
        filepathstr = os.path.join(folderpath,filename)
        #判断是文件再干活
        if os.path.isfile(filepathstr):            
            if fileflag == 0 :
                fileflag = 1 
                filelastmtime = datetime.datetime.fromtimestamp(os.stat(filepathstr).st_mtime)
                filelastmname = filepathstr
                continue
            if datetime.datetime.fromtimestamp(os.stat(filepathstr).st_mtime) > filelastmtime:
                filelastmtime = datetime.datetime.fromtimestamp(os.stat(filepathstr).st_mtime)
                filelastmname = filepathstr
#     print (filelastmname + '的修改时间为：' + str(filelastmtime))
    return filelastmname,filelastmtime,fileflag
shuiwu_nankang_gap_path = tools.readconfig('gap', 'shuiwu_nankang_gap_path')
result = getfolderlastmtime(shuiwu_nankang_gap_path)
print (result[0] + str(result[1]))
# result = getfolderlastmtime('E:\\python\\log')
# if not result[2]:
#     print ('空文件夹')
# filepath=tools.readconfig('gap', 'shuiwu_nankang_gap_path')
# print (os.path.isdir(filepath))
# print (os.path.normpath(filepath))
# print (os.path.join(filepath,'eclipse.rar'))

