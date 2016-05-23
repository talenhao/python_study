#!/usr/bin/env python3
# -*- coding:utf-8 -*-
def filetolist(file,listname):
    try:
        #打开文件
        with open(file) as jaf:
            #读取数据行
            data = jaf.readline()
        #转换成list
        listname=data.strip().split(',')
        return listname
    except IOError as ioerr:
        print('File error : %s' % ioerr)
        return(None)
        
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
    #使用列表推导式
    print('use list comprehension')
    cleanname2 = [sanitize(each_it) for each_it in thelist]
    print(sorted(cleanname2))
    #使用for 处理
#    sorted_name= sorted(cleanname2)
#    unique_name = 'unique_' + name
#    unique_name = []
#    for item in sorted_name:
#        if item not in unique_name:
#            unique_name.append(item)
#    print(unique_name[0:3])
    #使用工厂函数set()
    print(sorted(set(cleanname2))[0:3])
