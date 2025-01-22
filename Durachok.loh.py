import turtle
import random
score = 0

t = turtle.Turtle()
t.shape('turtle')


window = turtle.Screen()
window.title("")
window.bgcolor("white")
window.setup(width=800, height=600, startx=None, starty=None)

window.listen()

def move_forward():
    t.forward(10)

