#!/bin/env python3
#-*- coding:utf-8 -*-
'''
打印电影信息
version = 1.1.1
api evolustion:default value => set anathor bool value
'''
def print_lol(the_list, indent=False, level=0):
    for each_item in the_list:
        '''
        判断元素是否为列表类型.
        '''
        if isinstance(each_item, list) :
            print_lol(each_item, indent, level+1)
        else:
            '''
            是否启用新API
            '''
            if indent:
                for tab_stop in range(level):
                    print('\t',end='.')
            print(each_item)
