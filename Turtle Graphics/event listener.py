import random
from turtle import Turtle, Screen
screen = Screen()
t = Turtle()
t.shape("turtle")
t.width(30)
t.color("gray", "beige")
t.setheading(90)


def up():
    #t.left(90)
    t.forward(150)
    t.setheading(0)


def down():
    t.right(90)
    t.forward(150)
    t.setheading(0)


def right():
    t.right(90)
    t.forward(150)
    t.setheading(0)


def left():
    t.left(90)
    t.forward(150)
    t.setheading(0)


screen.onkeypress(fun=up, key="Up")
screen.onkeypress(fun=down, key="Down")
screen.onkeypress(fun=right, key="Right")
screen.onkeypress(fun=left, key="Left")

screen.listen()
screen.exitonclick()



