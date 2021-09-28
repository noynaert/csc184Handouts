import turtle
import random

def makeRandomColor():
    red = random.randrange(255)
    green=random.randrange(255)
    blue=random.randrange(255)
    color = red*256*256+green*256+blue
    return color

def polygon(t, sides, angle, distance):
    if sides==0:
       return
    else:
        #t.pencolor(makeRandomColor())
        t.forward(distance)
        t.right(angle)
        polygon(t, sides-1, angle, distance)

sides = 3
distance = 200
suzie = turtle.Turtle()
#suzie.pencolor("#ff0000")
#polygon(suzie, 4, 90, 100)
polygon(suzie, sides, 360/sides, distance)
turtle.done()