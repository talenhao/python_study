#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#使用cgi模块处理表单数据
import cgi
#cgi跟踪模块
import cgitb
cgitb.enable()
#将所有表单数据放在一个字典中
form_data = cgi.FieldStorage()
athlete_name = form_data['which_athlete'].value

import athletemodel,yate
#取出pickle数据
athletes = athletemodel.get_from_store()

#生成运动员时间显示页面
print(yate.start_response())
print(yate.include_header("时间数据信息"))
print(yate.header("运动员:" + athlete_name + ", 出生日期:" + athletes[athlete_name].dob + "."))
print(yate.para("最佳三次成绩为:"))
print(yate.u_list(athletes[athlete_name].top3))
print(yate.include_footer({"Home":"/index.html","其他成员数据":"generate_list.py"}))