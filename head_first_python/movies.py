#!/bin/env python3
#-*- coding:utf8 -*-
import nester
movies = ['The Holy Grail', 1975, 'Terry Jones & Terry Gilliam', 91, ['Graham Chapman', ['Michael Palin', 'John Cleese', 'Terry Gilliam', 'Eric Idle', 'Terry Jones']]]
def versions(version):
    print('version is %s' % version)
versions('1.1.0')
nester.print_lol(movies)
versions('1.1.1')
nester.print_lol(movies,1)
versions('1.2.0')
nester.print_lol(movies, 'Ture', 2)
