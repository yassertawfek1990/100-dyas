from turtle import Turtle, Screen
import random

tur = Turtle()
sc = Screen()
sc.colormode(255)

speed = 1
thick = 0
for i in range(300):
    tur.pensize(thick)
    tur.speed(speed)
    tur.forward(random.randint(30, 100))
    tur.right(360/(random.choice([2,4])))
    
    r = random.randrange(0, 257, 10)
    g = random.randrange(0, 257, 10)
    b = random.randrange(0, 257, 10)
    tur.color(r, g, b)
    speed += 0.5
    thick += 0.1









sc.exitonclick()