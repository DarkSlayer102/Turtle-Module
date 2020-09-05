import turtle
import random


class Square:

    def __init__(self, forward, backwards, right, left):
        self.forward = forward
        self.backwards = backwards
        self.right = right
        self.left = left

    def first_square(self):
        s = turtle.Turtle()
        bg_color = ['#7D7DFF', '#FFFF5C', '#828282', '#530000']
        turtle.bgcolor(random.choice(bg_color))
        s.color('#123650', '#3f343a')
        s.begin_fill()
        s.color('#fd5800', '#c154c1')
        s.forward(self.forward)
        s.left(self.left)
        s.forward(self.forward)
        s.left(self.right)
        s.forward(self.forward)
        s.left(self.left)
        s.forward(self.forward)
        s.end_fill()

    def second_square(self):
        second_turtle = turtle.Turtle()
        # background color
        turtle.bgcolor("#a800e6")
        # color
        second_turtle.color("#00e635", "#d0ff34")
        # making it unseen
        second_turtle.penup()
        second_turtle.backward(90)
        second_turtle.pendown()
        # fill in the shape color
        second_turtle.begin_fill()
        second_turtle.backward(self.backwards)
        second_turtle.left(self.left)
        second_turtle.forward(self.backwards)
        # changing color
        second_turtle.color('#fffb34', '#35ff97')
        second_turtle.right(self.right)
        second_turtle.forward(self.forward)
        second_turtle.right(90)
        second_turtle.forward(self.forward*5/5)
        second_turtle.end_fill()
    # easy way of making a square

    def three_square(self):
        ts = turtle.Turtle()
        colors = ['#6200A3', '#D5BDE7', '#003500', '#90EE90']

        ts.penup()
        ts.backward(100)
        ts.right(90)
        ts.forward(100)
        ts.pendown()
        ts.shape('turtle')
        ts.begin_fill()
        for i in range(4):
            bg_color = ['#7D7DFF', '#FFFF5C', '#828282', '#530000']
            turtle.bgcolor(random.choice(bg_color))
            ts.color(random.choice(colors))
            ts.forward(self.forward)
            ts.right(self.left)
        ts.end_fill()
        turtle.done()


s1 = Square(100, 100, 90, 90)
s1.first_square()
s1.second_square()
s1.three_square()
