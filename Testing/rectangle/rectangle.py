import turtle
import math
import random


class Rectangle:

    def __init__(self, forward, backwards, left, right):
        self.forward = forward
        self.backwards = backwards
        self.left = left
        self.right = right

    def rectangle1(self, x, y, b, c):
        r = turtle.Turtle()
        turtle.bgcolor('green')
        r.color('yellow', 'skyblue')
        r.begin_fill()
        r.forward(x)
        r.left(y)
        r.forward(c)
        r.left(y)
        r.forward(b)
        r.left(y)
        r.forward(c)
        r.end_fill()



r1 = Rectangle(100, 100, 90, 90)
r1.rectangle1(60, 90, 60, 200)

