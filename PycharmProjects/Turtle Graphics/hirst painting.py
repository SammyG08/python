import turtle, random
from turtle import Turtle, Screen

screen = Screen()
colors = ("yellow","brown","blue","gray","purple","violet","orange","indigo","turquoise","pink")
t = Turtle()
t.speed("fastest")
t.hideturtle()

for iteration in range(500):
    x_axis = random.randrange(-200,200,10)
    y_axis = random.randrange(-200,200,10)
    t.penup()
    t.goto(x_axis,y_axis)
    t.pendown()
    t.dot(30,random.choice(colors))

screen.exitonclick()
