import turtle
#from turtle import *

myTurtle = turtle.Turtle()

def square(sue):
    sue.forward(100)
    sue.right(90)
    sue.forward(100)
    sue.right(90)
    sue.forward(100)
    sue.right(90)
    sue.forward(100)
    sue.right(90)

def polygon(mine, sides, angle,distance):
    if sides==0:
        return
    else:
        mine.forward(distance)
        mine.right(angle)
        polygon(mine,sides-1,angle,distance)

myTurtle = turtle.Turtle()
#square(myTurtle)
polygon(myTurtle,300,360./300,1)  # We just invented integral calculus!
turtle.done()