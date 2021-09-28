# very basic turtle graphics in Python 3

import turtle
#from turtle import *

yertle = turtle.Turtle()
turtle.delay(100)
turtle.pencolor('red')
yertle.shape("turtle")  #because the triangle is boring.
yertle.forward(100)
print(turtle.heading())
yertle.right(90)
turtle.color('blue')
print(turtle.heading())
yertle.forward(100)

print("Screensize is",turtle.screensize())

