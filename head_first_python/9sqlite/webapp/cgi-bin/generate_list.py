#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#导入M,V
import athletemodel, yate

#生成一个选择运动员列表html页面
athletes=athletemodel.get_nameid_from_store()
print(yate.start_response())
print(yate.include_header("NUAC的运动员列表"))

print(yate.start_form("generate_timing_data.py"))
print(yate.para("从列表中选择一个运动员:"))
for each_athlete in athletes:
    #(name,id)
    print(yate.radio_button_id("which_athlete",each_athlete[0],each_athlete[1]))
print(yate.end_form("查看数据"))
print(yate.start_form("add_timing_data.py"))
print(yate.para("从列表中选择一个运动员:"))
for each_athlete in athletes:
    #(name,id)
    print(yate.radio_button_id("which_athlete",each_athlete[0],each_athlete[1]))
print(yate.end_form("添加数据"))
print(yate.include_footer({"Home":"/index.html"}))