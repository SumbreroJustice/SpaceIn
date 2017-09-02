#set up the screen
import tkinter
from tkinter import *
import turtle
import os


#Create Screen
wn = turtle.Screen()
wn.bgcolor("Black")
wn.title("Space Invaders")


#Create playable screen
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.penup()
border_pen.color("white")
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#Create Player
player = turtle.Turtle()
player.color("blue")
player.shape("square")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(45)


#Create Enemy
alien = turtle.Turtle()
alien.color("green")
alien.shape("circle")
alien.penup()
alien.speed(0)
alien.setposition(-200, 250 )



playerspeed = 12
alienspeed = 3

def moveleft():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)

def moveright():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

#Move
turtle.listen()
turtle.onkey(moveleft, "Left")
turtle.onkey(moveright, "Right")

while True:
    x = alien.xcor()
    x += alienspeed
    alien.setx(x)
    if x > 280:
        alienspeed = alienspeed * -1
        y = alien.ycor()
        y -= 40
        alien.sety(y)



    if x < -280:
        alienspeed = alienspeed * -1
        y = alien.ycor()
        y -= 40
        alien.sety(y)


delay = input('press enter to finsh')
