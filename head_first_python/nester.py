#!/bin/env python3
#-*- coding:utf-8 -*-
'''
打印电影信息
version = 1.1.0
'''
def print_lol(the_list, level):
    for each_item in the_list:
        '''
        判断元素是否为列表类型.
        '''
        if isinstance(each_item, list) :
            print_lol(each_item, level+1)
        else:
            for tab_stop in range(level):
                print('\t',end='.')
            print(each_item)
