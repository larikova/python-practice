import turtle
import random

lines = random.randint(0, 50)
length = random.randint(0, 50)
angle = random.randint(0, 180)

for i in range(0, lines):
    turtle.forward(length)
    turtle.left(angle)

