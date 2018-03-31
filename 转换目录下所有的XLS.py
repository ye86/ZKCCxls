# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 17:45:12 2018

@author: yefang
"""

import os
import glob
import convertXLS

# 默认返回当前目录下的 xls文件列表
def findfiles(dirname=0,pattern='*.xls'):   
    cwd = os.getcwd() #保存当前工作目录
    if dirname == 0:
        dirname = cwd
    if dirname:
        os.chdir(dirname)

    result = []
    for filename in glob.iglob(pattern): #此处可以用glob.glob(pattern) 返回所有结果
        result.append(filename)
    #恢复工作目录
    os.chdir(cwd)
    return result

def text():
    xlslist = findfiles() # 获得本目录下的所有xls文件
    for i in xlslist:     # 依次获得每个xls文件名
        if i[:4] != 'new_':    # 转换除“new_”开头的xls文件
            convertXLS.convertXLS(i)
    

if __name__ == '__main__': 
    text()