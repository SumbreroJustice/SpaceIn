#set up the screen
import tkinter
from tkinter import *
import turtle
import os

wn = turtle.Screen()
wn.bgcolor("Black")
wn.title("Space Invaders")

border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.penup()
border_pen.color("blue")

delay = input('press enter to finsh')
