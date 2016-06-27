#!/usr/bin/env python3
#-*- coding:utf-8 -*-
import turtle

def DrawSpiral(t,length, color, colorBase):
    if length == 0:
        return
    newcolor = (int(color[1:],16) + 2**10)%(2**24)
    base = int(colorBase[1:],16)
    if newcolor < base:
        newcolor = (newcolor + base)%(2**24)
    newcolor = hex(newcolor)[2:]
    newcolor = "#"+("0"*(6-len(newcolor)))+newcolor
    
    t.color(newcolor)
    t.forward(length)
    t.left(90)
    DrawSpiral(t, length-1, newcolor, colorBase)
def main():
    t = turtle.Turtle()
    screen = t.getscreen()
    t.speed(speed=100)
    t.penup()
    t.goto(-100,-100)
    t.pendown()
    DrawSpiral(t, 200, "#000000", "#ff00ff")
    screen.exitonclick()
if __name__ == "__main__":
    main()
