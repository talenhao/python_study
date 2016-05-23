#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#函数与处理的数据打包一起.
def filetolist(file,listname):
    try:
        #打开文件
        with open(file) as jaf:
            #读取数据行
            data = jaf.readline()
        #转换成list
        listname=data.strip().split(',')
        data = {}
        data['name'] = listname.pop(0)
        data['dob']  = listname.pop(0)
        data['time'] = listname
        result = print(data['name'] + '的三次最佳成绩是' + str(sorted(set([sanitize(each_it) for each_it in data['time']]))[0:3]))
        #return listname
        return result
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
    #使用列表
    #username=name+'user'
    #userdob =name+'dob'
    #username = thelist.pop(0)
    #userdob  = thelist.pop(0)
    ##使用列表推导式
    #name2 = [sanitize(each_it) for each_it in thelist]
    ##使用工厂函数set()
    #try:
    #    print(username + '的最佳成绩是' + str(sorted(set(name2))[0:3]))
    #except TypeError as typerr:
    #    print('list type error %s' % typerr)
    #使用字典

