#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#使用cgi模块处理表单数据
import cgi
#cgi跟踪模块
import cgitb
cgitb.enable()

import athletemodel,yate
#将所有表单数据放在一个字典中
form_data = cgi.FieldStorage()
athlete_id = form_data['which_athlete'].value
athlete=athletemodel.get_athlete_from_id(athlete_id)

#生成运动员时间显示页面
print(yate.start_response())
print(yate.include_header("NUAC时间数据信息"))
print(yate.header("运动员:" + athlete['Name'] + ", 出生日期:" + athlete['Dob'] + "."))
print(yate.para("最佳三次成绩为:"))
print(yate.u_list(athlete['Top3']))
print(yate.para("所有成绩条目: " + str(athlete['Data']) + "(重复数据已经移除.)."))
print(yate.include_footer({"Home":"/index.html","其他成员数据":"generate_list.py"}))
