#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
class athlete:
    def __init__(self, athlete_name, athlete_dob=None, athlete_times=[]):
        self.name = athlete_name
        self.dob  = athlete_dob
        self.times= athlete_times
    #运动员最好的3组成绩
    def top3(self):
        return(sorted(set([sanitize(time) for time in self.times]))[0:3])
    #为运动员添加一个成绩
    def add_time(self, time_value):
        self.times.append(time_value)
    #为运动员添加一组成绩,使用列表类型.
    def add_times(self, time_list):
        self.times.extend(time_list)
#使用类继承,继承内置list类
class athletelist(list):
    def __init__(self, a_name, a_dob=None, a_times=[]):
        list.__init__([])
        self.name = a_name
        self.dob  = a_dob
        self.extend(a_times)
    def top3(self):
        return(sorted(set([sanitize(t) for t in self]))[0:3])

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


talen = athlete('talen')
talen.add_time('3.25')
talen.add_time('3.45')
talen.add_times(['1.30','2.59'])
print(str(talen.top3()))
ken = athletelist('ken')
#为运动员添加一个成绩
#由于继承list,不需要自己再定义添加方法,直接使用list的方法
ken.append('4.25')
#为运动员添加一组成绩,使用列表类型.
ken.extend(['4.56','6.20','5.20'])
print(ken.top3())
