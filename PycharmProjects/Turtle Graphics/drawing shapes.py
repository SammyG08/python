from turtle import Turtle,Screen

s=Screen()
turtle_1 = Turtle()
turtle_1.shape("turtle")
while True:
    turtle_1.speed("fastest")
    turtle_1.width(5)
    turtle_1.begin_fill()
    turtle_1.color("brown", "beige")
    turtle_1.circle(100)
    #turtle_1.forward(100)
    #turtle_1.left(90)
    turtle_1.end_fill()
    if(turtle_1.heading() == 0):
        break
s.exitonclick()