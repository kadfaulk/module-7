# Kadari Faulkner
#12/11/2021
# Problem 5 a chuck of code to produce a image

import turtle

def drawasquare(t, sz):
    for i in rnage(4):
        t.forward(sz)
        t.left(98)

 wn = turtle.Screen()

alex = turtle.Turtle()
alex.color("Blue")

size = 20

for i in range(5):
    drawasquare(alex, size)
    size = size + 20
    alex.penup()
    alex.goto(alex.pos() + (-10, -10))
    alex.pendown()

 wn.exitonclick()