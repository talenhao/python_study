#!/usr/bin/env python3
#-*- coding:utf-8 -*-
#This imports the turtle graphics module.
import turtle


#The main function is where the main code of the program is written.
def main():
    #This line reads a line of input from the user.
    filename = input("Please enter drawing filename: ")
    #Create a Turtle Graphics window to draw in.
    t = turtle.Turtle()
    #This screen is used at the end of the program.
    screen = t.getscreen()
    file = open(filename,'r')
    command=file.readline().strip()
    while command != "":
        if command == "goto":
            x = float(file.readline())
            y = float(file.readline())
            width = float(file.readline())
            color = file.readline().strip()
            t.width(width)
            t.pencolor(color)
            t.goto(x,y)
        elif command == "circle":
            radius = float(file.readline())
            width = float(file.readline())
            color = file.readline().strip()
            t.width(width)
            t.pencolor(color)
            t.circle(radius)
        elif command == "beginfill":
            color = file.readline().strip()
            t.fillcolor(color)
            t.begin_fill()
        elif command == "endfill":
            t.end_fill()
        elif command == "penup":
            t.penup()
        elif command == "pendown":
            t.pendown()
        else:
            print("Unknown command found in file:",command)
        command=file.readline().strip()
    file.close()
    t.ht()
    screen.exitonclick()
    print("Program Execution Completed.")
if __name__ == "__main__":
    main()
