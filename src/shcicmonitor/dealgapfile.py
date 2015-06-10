# -*- coding:UTF-8 -*-
'''
Created on 2015年5月27日

@author: zjc
'''
import os
import datetime
import tools
def getfolderlastmtime(folderpath):
    '''
    获取文件夹中最后修改的文件名称和时间，用于网闸同步监控，不检查子文件夹
    参数：folderpath 文件名
    返回值：文件名称 string , 最后修改时间 datetime ,检查结果：0 正常，1 异常
    '''
    filelastmtime = None
    filelastmname = None
    fileflag = 1  # 初始化标志
    # 如果不是文件夹，立刻返回
    if not os.path.isdir(folderpath):
        return filelastmname, filelastmtime, fileflag
    # 遍历文件
    for filename in os.listdir(path=folderpath):
        filepathstr = os.path.join(folderpath, filename)
        # 判断是文件再干活
        if os.path.isfile(filepathstr):            
            if fileflag == 1 :
                fileflag = 0 
                filelastmtime = datetime.datetime.fromtimestamp(os.stat(filepathstr).st_mtime)
                filelastmname = filepathstr
                continue
            if datetime.datetime.fromtimestamp(os.stat(filepathstr).st_mtime) > filelastmtime:
                filelastmtime = datetime.datetime.fromtimestamp(os.stat(filepathstr).st_mtime)
                filelastmname = filepathstr
    tools.writeLog('网闸[' + folderpath + ']下最后修改的文件名称：' + os.path.basename(filelastmname) + ' ;最后修改时间为：' + str(filelastmtime))
    return filelastmname, filelastmtime, fileflag

def checkgap(gappath, gapsyndays):
    '''
    根据网闸文件最后修改时间检查网闸工作情况
    返回值：result: 0-正常，1-有过同步，但异常 , 2-网闸目录不存在，或者目录下没有文件  ; 最后修改时间  string
    '''
    result = getfolderlastmtime(gappath)
    # 有结果的话，进行时间判断
    if result[2] != 1 :
        legalday = datetime.datetime.now() - datetime.timedelta(days=gapsyndays)
        if result[1] <= legalday:
            tools.writeLog('网闸[' + gappath + ']检查完毕，结果：异常')
            return 1,result[1].strftime('%Y-%m-%d %H:%M:%S')  # 异常，需处理
        else:
            tools.writeLog('网闸[' + gappath + ']检查完毕，结果：正常')
            return 0,result[1].strftime('%Y-%m-%d %H:%M:%S')  # 没问题
    else:
        tools.writeLog('网闸文件夹下没文件，异常！')
        return 2,result[1]
        
if __name__ == '__main__':
    gap_path = tools.readconfig('gap', 'shuiwu_nankang_gap_path')
    gapdays = tools.readconfig('gap', 'shuiwu_nankang_gap_time')
    result = checkgap(gap_path, int(gapdays))
    print (result)

    
    
