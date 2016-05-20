#!/bin/env python3
#-*- coding:utf-8 -*-
'''
打印电影信息
version = 1.1.1
api evolustion:default value => set anathor bool value
'''
#20160520:添加输出参数设定
import sys
def print_lol(the_list, indent=False, level=0, fh=sys.stdout):
    for each_item in the_list:
        '''
        判断元素是否为列表类型.
        '''
        if isinstance(each_item, list) :
            print_lol(each_item, indent, level+1, fh)
        else:
            '''
            是否启用新API
            '''
            if indent:
                for tab_stop in range(level):
                    print('\t',end='.', file=fh)
            print(each_item, file=fh)
