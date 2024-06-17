from turtle import Turtle, Screen, colormode

import random

tur = Turtle()
sc = Screen()
sc.colormode(255)
tur.speed("fastest")
n = 0
for i in range(360):
    tur.circle(100)
    tur.right(n)
    r = random.randrange(0, 257, 10)
    g = random.randrange(0, 257, 10)
    b = random.randrange(0, 257, 10)
    tur.color(r, g, b)
    n += 1

sc.exitonclick()