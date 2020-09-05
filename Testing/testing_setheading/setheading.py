import turtle
import random


def making_something(x, y, a, b):
    t = turtle.Turtle()
    bg_color = ['#7D7DFF', '#FFFF5C', '#828282', '#530000']
    turtle.bgcolor(random.choice(bg_color))
    colors = ['#6200A3', '#D5BDE7', '#003500', '#90EE90']
    t.pensize(5)

    def up():
        t.setheading(90)
        t.forward(100)

    def down():
        t.setheading(270)
        t.forward(100)
        t.circle(90)

    def left():
        t.setheading(180)
        t.forward(100)

    def right():
        t.setheading(0)
        t.forward(100)

    def clickleft(x, y):
        t.color(random.choice(colors))

    def clickright(x, y):
        t.stamp()

    turtle.listen()

    turtle.onclick(clickleft, 1)
    turtle.onclick(clickright, 3)
    turtle.onkey(up, 'Up')
    turtle.onkey(down, 'Down')
    turtle.onkey(left, 'Left')
    turtle.onkey(right, 'Right')

    turtle.done()


making_something(100, 100, 90, 90)
