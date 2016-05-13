#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
'''
import sqlite3, sys

# 连接数据库
conn = sqlite3.connect('food.db')
cursor = conn.cursor()

# query = 'select * from food where %s' % sys.argv[1]
query = 'select * from food'
print(query)
cursor.execute(query)
name = [f[0] for f in cursor.description]
print
cursor.description
print(name)
for row in cursor.fetchall():
    print
    row
    for pair in zip(name, row):
        print('%s:%s' % pair)
conn.close()
