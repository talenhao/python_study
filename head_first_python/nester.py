#!/bin/env python3
#-*- coding:utf-8 -*-
'''
打印电影信息
'''
def print_lol(the_list):
    for each_item in the_list:
        '''
        判断元素是否为列表类型.
        '''
        if isinstance(each_item, list) :
            print_lol(each_item)
        else:
            print(each_item)
