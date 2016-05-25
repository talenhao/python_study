#!/usr/bin/evn python3
# -*- coding:utf8 -*-
'''
1.读取文件	=>	put_to_store	=>	pickle
2.pickle      	=>	get_from_store	=>	viewer 
'''
import pickle
from kelly_c import athletelist
#磁盘文件处理
def openfile(filename):
    try:
        #打开文件
        with open(filename) as athlete_file:
            #读取数据
            data = athlete_file.readline()
            #初步处理数据,去空,以,号分割
            value_list= data.strip().split(',')
            #分别取出有格式的三种数据
            username = value_list.pop(0)
            userdob  = value_list.pop(0)
            usertimes= value_list
            #返回实例对象
            athlete_instance=athletelist(username,userdob,usertimes)
            return(athlete_instance)
    except IOError as ioerr:
        print('File error %s' % ioerr)
        return(None)

#内容压制,使用字典数据类型.
def put_to_store(files_list):
    #字典生成
    all_athletes = {}
    for each_file in files_list:
        each_athlete = openfile(each_file)
        all_athletes[each_athlete.name] = each_athlete
    #pickle数据压制
    try:
        with open('data/athletes.pickle','wb') as athlfile:
            pickle.dump(all_athletes,athlfile)
    except IOError as ioerr:
        print('File error(%s)' % ioerr)
    return(all_athletes)

def get_from_store():
    all_athletes = {}
    #pickle数据解压
    try:
        with open('data/athletes.pickle','rb') as athlfile:
            all_athletes=pickle.load(athlfile)
    except IOError as ioerr:
        print('File error(%s)' % ioerr)
    return(all_athletes)

#files_list = ["../data/james.txt", "../data/julie.txt", "../data/mikey.txt", "../data/sarah.txt"]
#data = put_to_store(files_list)
#test
'''
print(get_from_store())
print(dir())
type(data)
print('Use put_to_store()')
for each_athlete in data:
    print(data[each_athlete].name,data[each_athlete].dob)
print('Use get_from_store()')
data_copy = get_from_store()
for each_athlete in data_copy:
    print(data_copy[each_athlete].name,data_copy[each_athlete].dob)
'''