#!/bin/env python3
#-*- coding:utf8 -*-
'''
Black hat python
'''
import socket
target_host = 'www.baidu.com'
target_port = 80
#Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connect the client
client.connect((target_host,target_port))#tuple:(ip:port)
#Send some data
client.send(b"GET / HTTP/1.1\r\nHost:baidu.com\r\n\r\n")#duoble \r\n is end of head
#Receive some data
response = client.recv(4096)
print(response)
