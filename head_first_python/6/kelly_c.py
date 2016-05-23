#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
class athlete:
    def __init__(self, athlete_name, athlete_dob=None, athlete_times=[]):
        self.name = athlete_name
        self.dob  = athlete_dob
        self.times= athlete_times
    def top3(self):
        return(sorted(set([sanitize(time) for time in self.times]))[0:3])

def openfile(filename):
    try:
        #打开文件
        with open(filename) as athlete_file:
            #读取数据
            data = athlete_file.readline()
            value_list= data.strip().split(',')
            username = value_list.pop(0)
            userdob  = value_list.pop(0)
            usertimes= value_list
            #返回实例对象
            athlete_instance=athlete(username,userdob,usertimes)
            return(athlete_instance)
    except IOError as ioerr:
        print('File error %s' % ioerr)
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
    name = openfile(name+'.txt')
    print(name.name + '的三次最佳成绩是' + str(name.top3()))
