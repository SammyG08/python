import turtle,random
from turtle import Screen, Turtle

count = int(input("\n\n\nHow many turtles will take part in the race?\nIt should be between the range of 2-10.\nUser Response: "))
turtles = []
colors = ("blue","orange","indigo","turquoise")
s = Screen()
WIDTH = 400
HEIGHT = 300
x_spacing = WIDTH//(count + 1)


while True:
    if count >= 2:
        for i in range(1, count+1):
            t = Turtle()
            t.shape("turtle")
            t.fillcolor(random.choice(colors))
            t.pensize(70)
            t.hideturtle()
            t.penup()
            t.goto(-WIDTH//2+(i * x_spacing), -HEIGHT//2)
            t.left(90)
            t.showturtle()
            turtles.append(t)
            race_closed = True
        break
    else:
        print("\nInvalid input")
        break


def racing_logic():
    WINDOW_HEIGHT = 400
    winner_determined = False
    while not winner_determined:
        for list_turtle in turtles:
            distance = random.randrange(1,10)
            list_turtle.forward(distance)

            x_axis, y_axis = list_turtle.pos()
            if y_axis >= WINDOW_HEIGHT - 23:
                print(f"\nThe winner of the race is the {list_turtle.fillcolor()} turtle.")
                winner_determined = True


racing_logic()
s.exitonclick()
