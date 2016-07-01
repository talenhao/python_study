#!/bin/env python3
#-*- coding:utf-8 -*-
import flask
app=flask.Flask(__name__)
@app.route("/")
def index():
    return '<h1>Hello Talen!</h1>'
#添加动态路由
@app.route("/user/<name>")
def user(name):
    return "<H1>Hello %s!</H1>" % name
if __name__ == "__main__":
    app.run(debug=True)

