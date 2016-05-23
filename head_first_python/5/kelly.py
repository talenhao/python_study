#!/usr/bin/env python3
# -*- coding:utf-8 -*-
def filetolist(file,listname):
    #打开文件
    with open(file) as jaf:
        #读取数据行
        data = jaf.readline()
    #转换成list
    listname=data.strip().split(',')
    return listname

        
#处理字符,转换成m.s格式
def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return time_string
    (min, sec) = time_string.split(splitter)
    return (min + '.' + sec)

for name in ["james", "julie", "mikey", "sarah"]:
    thelist=filetolist(name+".txt",name)
    cleanname = 'clean' + name
    cleanname = []
    for each_t in thelist:
        cleanname.append(sanitize(each_t))
    print(sorted(cleanname))
