#!/usr/bin/env python3
#-*- coding:utf-8 -*-
'''
'''
import sqlite3

'''
打开文件
分段
整理字段

'''

def convert(value):
    if value.startswith('~'):
        return value.strip('~')
    if not value:
        value = 0
    return float(value)

#连接数据库
conn = sqlite3.connect('food.db')
cursors = conn.cursor()
cursors.execute('''
    CREATE TABLE food(
      id  TEXT  PRIMARY KEY,
      desc TEXT,
      water FLOAT,
      kcal FLOAT,
      protein FLOAT,
      fat FLOAT,
      ash FLOAT,
      carbs FLOAT,
      fiber FLOAT,
      sugar FLOAT
    )
''')
field_count = 10
#makers = '?,'.join(['%s'] * field_count)
#query='Insert into food VALUES (%s)' % makers
query = 'INSERT INTO food VALUES (?,?,?,?,?,?,?,?,?,?)'

for line in open('abbrev.txt'):
    fields = line.split('^')
    print(fields[:field_count])
    vals= [convert(f) for f in fields[:field_count]]
    print('vals is : %s' % vals)
    cursors.execute(query, vals)
#关闭数据库连接
conn.commit()
conn.close()
