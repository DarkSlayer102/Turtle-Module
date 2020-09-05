import turtle
import math
import random


class MyTurtle:
    def __init__(self, name, age, wow):
        self.name = name
        self.age = age
        self.wow = wow

    def first_turtle(self, forward, left, right, back, x, y, a, b):
        t = turtle.Turtle()
        t.begin_fill()
        turtle.bgcolor("black")
        t.color('blue')
        t.pensize(2)
        t.backward(100*4/2-60)
        t.color('red', 'yellow')
        t.goto(x, y)
        t.left(a)
        t.forward(b+30)
        t.right(600)
        t.forward(30)
        t.end_fill()

        return 'Wow'

    def second_turtle(self, x, y, g, t):
        st = turtle.Turtle()
        turtle.title('First Turtle Game')
        st.color('red', 'blue')
        st.pensize(5)
        st.dot(10, 'yellow')
        st.penup()
        st.sety(200/2)
        st.pendown()
        st.forward(20*5+50-50)
        st.color('skyblue', 'blue')
        st.begin_fill()
        st.speed(0)
        st.circle(2*5*10)
        st.end_fill()
        st.speed(10)
        st.shapesize(1, 1, 10)
        return 'Hi'

    def next_turtle(self, x, y):
        nt = turtle.Turtle()
        nt.fillcolor('orange')
        nt.penup()
        try:
            nt.forward(x)
        except:
            print("Error")
        nt.pendown()
        nt.pencolor('darkblue')
        nt.begin_fill()
        for i in range(6):
            nt.forward(120)
            nt.right(60)
        nt.end_fill()

        nt.penup()
        nt.backward(100)
        nt.right(90)
        nt.forward(100)
        nt.right(90)
        nt.forward(100)
        nt.pendown()
        nt.setheading(369)
        nt.forward(100)
        john = 20
        sam = 'sam'
        second = 2
        nt.begin_fill()
        while john > second:
            colors = ['#6200A3', '#D5BDE7', '#003500', '#90EE90']
            nt.color(random.choice(colors))
            nt.speed(0)
            nt.circle(random.randrange(2, 20))
            nt.left(360)
            nt.right(1060)
            nt.hideturtle()
            nt.showturtle()
            second += 1
        nt.end_fill()
        nt.penup()
        nt.forward(100)
        nt.left(270)
        nt.forward(100*2)
        nt.right(90)
        nt.forward(100)
        nt.left(450)
        nt.pendown()
        turtle.done()


mt1 = MyTurtle('Sam', 16, 'joking')
print(mt1.first_turtle(100, 20, 40, 20, -20, -40, 40, 20))
print(mt1.second_turtle(100, 420, 50, 20))
print(mt1.next_turtle(100, 90))
