#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#导入M,V
import athletemodel, yate
#glob 模块可以向操作系统查询一个文件名列表
import glob

#生成一个选择运动员列表html页面
data_files = glob.glob('data/*.txt')
athletes = athletemodel.put_to_store(data_files)

print(yate.start_response())
print(yate.include_header("kelly教练的运动员列表"))

print(yate.start_form("generate_timing_data.py"))
print(yate.para("从列表中选择一个运动员:"))
for each_athlete in athletes:
    print(yate.radio_button("which_athlete",athletes[each_athlete].name))
print(yate.end_form("Select"))


print(yate.include_footer({"Home":"/index.html"}))