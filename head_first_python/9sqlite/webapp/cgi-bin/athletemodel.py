#!/usr/bin/evn python3
# -*- coding:utf8 -*-

#使用sqlite3重构
from kelly_c import athletelist
import sqlite3
db_name = 'data/coachdata.sqlite'

#打印运动员的名字
def get_names_from_store():
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    cursor.execute("select name from athletes")
    response = [row[0] for row in cursor.fetchall()]
    return response
#返回运动员id信息
def get_nameid_from_store():
    connection=sqlite3.connect(db_name)
    cursor=connection.cursor()
    results=cursor.execute("SELECT name,id FROM athletes")
    response=results.fetchall()
    connection.close()
    return(response)
#返回运动员信息.
def get_athlete_from_id(athlete_id):
    connection=sqlite3.connect(db_name)
    cursor=connection.cursor()
    result=cursor.execute("SELECT name,dob FROM athletes WHERE id=? ",(athlete_id,))
    (name,dob)=result.fetchone()
    results=cursor.execute("SELECT value FROM timing_data WHERE athlete_id=?",(athlete_id,))
    data=[row[0] for row in results.fetchall()]
    response={  "Name":name,
                "Dob":dob,
                "Data":data,
                "Top3":data[0:3]
        }
    connection.close()
    return(response)
#a=get_athlete_from_id(3)
