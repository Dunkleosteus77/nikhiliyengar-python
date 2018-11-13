import turtle
pen = turtle.Pen()
turtle.window_height=100
turtle.window_width=100

def square():
    for x in range(100):
        pen.forward(50)
        pen.left(90)
        pen.stop(4)
    for x in range(100):
        pen.forward(90)
        pen.left(90)
square()

def rectangle():
    for x in range(100):
        pen.forward(60)
        pen.left(90)
        pen.forward(50)
        pen.left(90)
        pen.forward(60)
#rectangle()

def filledsquare():
    for x in range(100):
        pen.forward(x)
        pen.left(91)
#filledsquare()
