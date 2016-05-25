#!/usr/bin/env python3
# -*- coding:utf-8 -*-
class athletelist(list):
    def __init__(self, a_name, a_dob=None, a_times=[]):
        list.__init__([])
        self.name = a_name
        self.dob  = a_dob
        self.extend(a_times)
    @property
    def top3(self):
        return(sorted(set([sanitize(t) for t in self]))[0:3])
    @property
    def to_dict(self):
        return({
            'name':self.name,
            'dob':self.dob,
            'top3':self.top3      
            })

#处理字符,转换成m.s格式
def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return time_string
    (min, sec) = time_string.split(splitter)
    return (min + '.' + sec)
