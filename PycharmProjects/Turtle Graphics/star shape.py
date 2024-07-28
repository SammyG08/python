import turtle, random
from turtle import Turtle, Screen

screen = Screen()
display = Turtle()

turtle.colormode()
colors = ("yellow","brown","blue","gray","purple","violet","orange","indigo","turquoise","pink")
display.penup()
display.setposition(-200, 0)
display.pendown()
while True:
    display.width(5)
    display.speed("fastest")
    current_color = random.choice(colors)
    #blue = random.choice(colors)
    #green = random.choice(colors)
    display.pencolor(current_color)
    display.forward(400)
    display.lt(170)
    if display.heading() == 0:
        display.hideturtle()
        break

screen.exitonclick()