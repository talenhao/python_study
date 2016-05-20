#!/usr/bin/env python3
#-*- coding:utf8 -*-
try:
    #data = open('sketch1.txt')
    data = open('sketch.txt')
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':',1)
            print(role, end='')
            print(' said: ', end='')
            print(line_spoken, end='')
        except ValueError:
            pass
    data.close()
except IOError:
    print('The datafile is missing!')
