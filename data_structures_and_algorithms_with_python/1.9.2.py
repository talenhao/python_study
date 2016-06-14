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
    for line in file:
        text = line.strip()
        commandlist=text.split(",")
        command = commandlist[0]
        if command == "goto":
            x = float(commandlist[1])
            y = float(commandlist[2])
            width = float(commandlist[3])
            color = commandlist[4].strip()
            t.width(width)
            t.pencolor(color)
            t.goto(x,y)
        elif command == "circle":
            radius = float(commandlist[1])
            width = float(commandlist[2])
            color = commandlist[3].strip()
            t.width(width)
            t.pencolor(color)
            t.circle(radius)
        elif command == "beginfill":
            color = commandlist[1].strip()
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
    file.close()
    t.ht()
    screen.exitonclick()
    print("Program Execution Completed.")
if __name__ == "__main__":
    main()