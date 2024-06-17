from turtle import Turtle, Screen
import random

sc = Screen()
sc.colormode(255)



tur = Turtle()

tur.shape("arrow")
# tur.fd(100)
# tur.rt(90)
# tur.fd(100)
# tur.rt(90)
# tur.fd(100)
# tur.rt(90)
# tur.fd(100)

# for _ in range(15):
#     tur.forward(10)
#     tur.penup()
#     tur.forward(10)
#     tur.pendown()
n = 3
while n <= 9:
    r = random.randrange(0, 257, 10)
    g = random.randrange(0, 257, 10)
    b = random.randrange(0, 257, 10)
    tur.color(r, g, b)
    for x in range(n):
        tur.fd(100)
        tur.rt(360/n)
    
    n += 1 





sc.exitonclick()