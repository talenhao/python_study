#!/bin/env python3
#-*- coding:utf8 -*-
#use with as replace finally to process open file
#use pickle process data
import pickle
man = []
other = []
try:
    with open('sketch.txt') as data:
        for each_line in data:
            try:
                (role, line_spoken) = each_line.split(':',1)
                line_spoken=line_spoken.strip()
                if role == 'Man':
                    man.append(line_spoken)
                elif role == 'Other Man':
                    other.append(line_spoken)
            except ValueError:
                pass
except IOError as ioerr:
    print('The datafile is missing! %s' % ioerr)

try:
    #打开模式修改为wb,b代表二进制
    with open('man_data.txt', 'wb') as man_file:
        pickle.dump(man,man_file)
    with open('other_data.txt', 'wb') as other_file:
        pickle.dump(other,other_file)
except IOError as ioerr2:
    print('Wirte to file error! %s '% ioerr2)
#不要忘记处理pickle异常
except pickle.PickleError as perr:
    print('Pickleing error: %s ' % perr)


#读取pickle dump的文件

try:
    with open('man_data.txt', 'rb') as rman, open('other_data.txt', 'rb') as rother:
        rman_file = pickle.load(rman)
        rother_file = pickle.load(rother)
        print(rman_file)
        print(rother_file)
except IOError as IOE:
    print('file error %s'%IOE)
except pickle.PickleError as pperr :
    print('pickle error %s' % pperr)
