#!/bin/env python3
#-*- coding:utf8 -*-
man = []
other = []
try:
    data = open('sssketch.txt')
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
finally:
    print(locals())
    if 'data' in locals():
        data.close()
try:
    man_file = open('man_data.txt', 'w')
    other_file = open('other_data.txt', 'w')
    print(man, file=man_file)
    print(other, file=other_file)
except IOError as ioerr2:
    print('Wirte to file error! %s' % ioerr2)
finally:
    if man_file in locals():
        man_file.close()
    if other_file in locals():
        other_file.close()
