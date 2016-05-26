#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import yate
import sqlite3
import cgi
import cgitb
cgitb.enable()

import os,sys,time

print(yate.start_response('text/plain'))
#接收传递给py脚本的数据为字典,并赋给from
form=cgi.FieldStorage()
athlete_id = form_data['which_athlete'].value




addr = os.environ['REMOTE_ADDR']
host = os.environ['REMOTE_HOST']
method = os.environ['REQUEST_METHOD']

#当前时间
cur_time = time.asctime(time.localtime())

print(host,addr,cur_time,method,file=sys.stderr)

for each_form_item in form.keys():
    print(each_form_item,'->',form[each_form_item].value,end=' ',file=sys.stderr)
print(file=sys.stderr)

