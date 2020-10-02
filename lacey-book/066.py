import turtle
import random

turtle.pensize(4)
for i in range(0,8):
    turtle.color(random.choice(["red", "blue", "yellow", "green", "pink", "black"]))
    turtle.forward(150)
    turtle.right(45)



turtle.exitonclick()
