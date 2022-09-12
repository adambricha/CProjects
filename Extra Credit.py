#Adam Bricha U9233-5585
#The program takes a radius value, offset value, and number of circles
#value from the user. The program validates these inputs. The program then draws colored circles.

import turtle
import random

from random import randrange
random_color = (randrange(0,255), randrange(0,255), randrange(0,255))

Radius = int(input("Enter a radius >=10: "))

while Radius < 10:
    Radius = int(input("Please re-enter a radius >= 10: "))
offset = int(input("Enter a value to increase the radius of the next circle: (>=5: "))
while offset < 5:
    offset = int(input("Please re-enter an offset: "))
circles = int(input("How many circles to draw? Must be atleast 1: "))
while circles < 1:
    int(input("Please re-enter a value >=1: "))

window = turtle.Screen()
turtle.colormode(255)
turtle.speed(0)
for z in range(circles):
    turtle.circle(Radius+z,circles,offset)
    turtle.color(random_color,)


