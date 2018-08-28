#!/usr/bin/env python3

# 检查用户名n
database = [
    ['talen', 12345],
    ['alex', 23456],
    ['eric', 4566]
]
username = input('User name: ')
pin = input('PIN code: ')
print(type(pin))
if [username, int(pin)] in database:
    print(username, "Access granted!")
else:
    print(username, "Access Deny!")