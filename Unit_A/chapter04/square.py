# square.py

# draws a square as a function

import turtle

#function to draw a square of specified length
def drawSquare(t, length):
    # t is a turtle
    # length is the length of the side
    t.pencolor('red')
    t.forward(length)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.forward(length)
    t.left(90)

tubby = turtle.Turtle()
tubby.shape('turtle')
tubby.right(45)
sideLength = int(input ("How long is one side?"))
drawSquare(tubby, sideLength)
tubby.left(90)
drawSquare(tubby, sideLength)
tubby.left(90)
drawSquare(tubby, sideLength)
tubby.left(90)
drawSquare(tubby, sideLength)
turtle.done()