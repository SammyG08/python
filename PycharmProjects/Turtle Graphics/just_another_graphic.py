import turtle, random
from turtle import Turtle, Screen

screen = Screen()
colors = ("yellow","brown","blue","gray","purple","violet","orange","indigo","turquoise","pink")
t = Turtle()
t.width(15)
t.speed("fastest")
t.hideturtle()
for iteration in range(500):
    range_of = random.randrange(0,360,90)
    t.pencolor(random.choice(colors))
    t.setheading(range_of)
    t.forward(30)


screen.exitonclick()