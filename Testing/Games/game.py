import turtle
import random
import math


class Game:

    def __init__(self, forward, backwards, left, right):
        self.forward = forward
        self.backwards = backwards
        self.left = left
        self.right = right

   # background of game
    def setting(self, x, y):
        gs = turtle.Turtle()
        gs.pensize(5)
        turtle.title('My first game')
        turtle.bgcolor('blue')
        gs.color('yellow', 'black')
        gs.begin_fill()
        gs.penup()
        gs.hideturtle()
        gs.left(self.left*2)
        gs.forward(self.forward)
        gs.pendown()
        gs.showturtle()
        gs.right(self.right*3)
        gs.forward(self.forward*3)
        gs.left(y)
        gs.forward(self.forward*3)
        gs.left(90)
        gs.forward(self.backwards*6)
        gs.left(self.right)
        gs.forward(self.backwards*3)
        gs.left(90)
        gs.forward(self.backwards*3)
        gs.hideturtle()
        gs.end_fill()

    def players(self):
        p = turtle.Turtle()
        ok = turtle.textinput("username key", "Computer is white Color and Ur red Color|Press x to play the game")
        if ok == 'x':

            p.color('white')
            p.pensize(5)
            p.penup()
            p.left(self.left*3)
            p.forward(self.forward*3)
            p.left(180)
            p.forward(20)
            p.pendown()

            p1 = turtle.Turtle()
            p1.color("red")
            p1.hideturtle()
            p1.penup()
            p1.pensize(5)
            p1.penup()
            p1.left(self.left*3)
            p1.forward(self.forward*3)
            p1.left(180)
            p1.forward(20)
            p1.left(270)
            p1.forward(70)
            p1.left(self.left)
            p1.showturtle()
            p1.pendown()

            def up():
                p1.setheading(90)
                p1.shape('turtle')
                p1.speed(0)
                p1.forward(100*5+60)

            turtle.listen()

            turtle.onkey(up, 'Up')
            p.forward(100*5+60)
            turtle.done()


g1 = Game(100, 100, 90, 90)
g1.setting(100, 90)
g1.players()
