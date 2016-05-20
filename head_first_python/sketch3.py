#!/bin/env python3
#-*- coding:utf8 -*-
#use with as replace finally to process open file

import nester
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
    with open('man_data.txt', 'w') as man_file:
        #use nester.print_lol() format list and write to file   
        nester.print_lol(man, 'True', 1, fh=man_file)
        #print(man, file=man_file)
    with open('other_data.txt', 'w') as other_file:
        nester.print_lol(other, 'True', 1, fh=other_file)
        #print(other, file=other_file)
except IOError as ioerr2:
    print('Wirte to file error! %s '% ioerr2)
