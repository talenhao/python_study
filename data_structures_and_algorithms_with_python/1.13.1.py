#!/usr/bin/env python3
#-*- coding:utf-8 -*-
#This imports the turtle graphics module.
import turtle

class GoToCommand:
    #----------------------------------------------------------------------
    def __init__(self,x,y,width=1,color="black"):
        """"""
        self.x=x
        self.y=y
        self.width=width
        self.color=color
    #----------------------------------------------------------------------
    def draw(self,turtle):
        """"""
        turtle.width(self.width)
        turtle.pencolor(self.color)
        turtle.goto(self.x, self.y)
########################################################################
class CirCleCommand:
    """"""
    #----------------------------------------------------------------------
    def __init__(self,radius,width=1,color="black"):
        """Constructor"""
        self.radius=radius
        self.width=width
        self.color=color
    #----------------------------------------------------------------------
    def draw(self,turtle):
        """"""
        turtle.width(self.width)
        turtle.pencolor(self.color)
        turtle.circle(self.radius)
########################################################################
class BeginFillCommand:
    """"""

    #----------------------------------------------------------------------
    def __init__(self,color):
        """Constructor"""
        self.color=color
    #----------------------------------------------------------------------
    def draw(self,turtle):
        """"""
        turtle.fillcolor(self.color)
        turtle.begin_fill()
########################################################################
class EndFillCommand:
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        pass
    #----------------------------------------------------------------------
    def draw(self,turtle):
        """"""
        turtle.end_fill()
########################################################################
class PenUpCommand:
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        pass
    #----------------------------------------------------------------------
    def draw(self,turtle):
        """"""
        turtle.penup()
########################################################################
class PenDownCommand:
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        pass
    #----------------------------------------------------------------------
    def draw(self,turtle):
        """"""
        turtle.pendown()

########################################################################
class PyList:
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        self.items=[]
    #----------------------------------------------------------------------
    def append(self,item):
        """"""
        self.items.append(item)
    #----------------------------------------------------------------------
    def __iter__(self):
        """"""
        for c in self.items:
            yield c
        
    
    
#The main function is where the main code of the program is written.   
def main():
    #This line reads a line of input from the user.
    filename = input("Please enter drawing filename: ")
    #Create a Turtle Graphics window to draw in.
    t = turtle.Turtle()
    #This screen is used at the end of the program.
    screen = t.getscreen()
    file = open(filename,'r')
    GraphicsCommands = PyList()
    command=file.readline().strip()
    while command != "":
        if command == "goto":
            x = float(file.readline())
            y = float(file.readline())
            width = float(file.readline())
            color = file.readline().strip()
            cmd = GoToCommand(x, y, width, color)
        elif command == "circle":
            radius = float(file.readline())
            width = float(file.readline())
            color = file.readline().strip()
            cmd=CirCleCommand(radius, width, color)
        elif command == "beginfill":
            color = file.readline().strip()
            cmd=BeginFillCommand(color)
        elif command == "endfill":
            cmd=EndFillCommand()
        elif command == "penup":
            PenUpCommand()
        elif command == "pendown":
            PenDownCommand()
        else:
            raise RuntimeError("Unknown command found in file:"+command)
        
        GraphicsCommands.append(cmd)
        command=file.readline().strip()
    for cmd in GraphicsCommands:
        cmd.draw(t)
    file.close()
    t.ht()
    screen.exitonclick()
    print("Program Execution Completed.")


if __name__ == "__main__":
    main()
