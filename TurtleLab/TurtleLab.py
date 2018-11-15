import turtle
pen = turtle.Pen()
turtle.window_height=100
turtle.window_width=100
turtle.bgcolor("black")

def square():
    for x in range(4):
        pen.pencolor("blue")
        pen.forward(50)
        pen.left(90)
    pen.penup()
    pen.setpos(0,-130)
    pen.pendown()
    for x in range(4):
        pen.forward(50)
        pen.left(90)
    pen.penup()
#square()

def rectangle():
    pen.setpos(-5,60)
    pen.pendown()
    pen.pencolor("green")
    pen.forward(60)
    pen.left(90)
    pen.forward(50)
    pen.left(90)
    pen.forward(60)
    pen.left(90)
    pen.forward(50)
    pen.left(90)
    pen.penup()
    pen.setpos(-5,-60)
    pen.pendown()
    pen.forward(60)
    pen.left(90)
    pen.forward(50)
    pen.left(90)
    pen.forward(60)
    pen.left(90)
    pen.forward(50)
    pen.left(90)
#rectangle()

def circle():
    pen.setpos(-50,0)
    pen.pendown()
    pen.color("red")
    pen.forward(100)
    pen.penup()
    pen.setpos(-100,-100)
    pen.pendown()
    for x in range(4):
        pen.forward(200)
        pen.left(90)
    pen.penup()
    pen.setpos(0,-300)
    pen.down()
    pen.color(0,1,0)
    pen.circle(300)
    pen.penup()
    pen.setpos(-200,-150)
    pen.pendown()
    pen.color("#427af4")
    for x in range(3):
        pen.forward(400)
        pen.left(120)
#circle()

def advanced():
    color=input("Do you want green, blue, red, purple, or yellow ")
    if color == "green" or "blue" or "red" or "purple" or "yellow":
        pen.color(color)
    if color != "green" or "blue" or "red" or "purple" or "yellow":
        print("I don't know what that is, so I picked red for you")
        pen.color("red")
    sides=int(input("How many sides do you want? "))
    length=int(input("How long is each side? "))
    if sides > 2:
        angle=(180*(sides-2))/sides
    if sides > 2 and length <= 500 and length >= 50:
        for x in range(sides):
            pen.forward(length)
            pen.left(180-angle)
    elif sides <= 2 and length > 50 and length <= 500:
        print("We make shapes here. I made you a triangle so you can get the gist here")
        for x in range(3):
            pen.forward(length)
            pen.left(120)
    elif length > 500 and sides > 2:
        print("That's a very big number that I can't be bothered to deal with, so enjoy that at 200 px")
        for x in range(sides):
            pen.forward(200)
            pen.left(180-angle)
    elif length < 50 and sides > 2:
        print("Have you considered that length's too small? I drew it at 200 px instead")
        for x in range(sides):
            pen.forward(200)
            pen.left(180-angle)
    elif sides <=2 and length < 50 or sides <=2 and length > 500:
        print("You have broken the system. You will get a red triangle and you will like it")
        pen.color("red")
        for x in range(3):
            pen.forward(200)
            pen.left(120)
advanced()

turtle.update()
turtle.exitonclick()
