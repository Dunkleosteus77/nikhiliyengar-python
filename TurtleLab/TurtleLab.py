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

def main():
    count=int(input("How many shapes do you want? "))
    for x in range(count):
        advanced()

def advanced():
    color=input("Do you want green, blue, red, purple, or yellow? ")
    if color == "green" or color == "blue" or color=="red" or color=="purple" or color=="yellow":
        pen.color(color)
    elif color != "green" or color != "blue" or color != "red" or color != "purple" or color != "yellow":
        print("I don't know what that is, so I picked red for you")
        pen.color("red")
    sides=int(input("How many sides do you want? "))
    if sides == 2 or sides == 1 or sides < 0:
        print("We make shapes here. I made you a triangle so you can get the gist here")
        sides=3
    length=int(input("How long is each side? "))
    if length > 500:
        print("That's a very big number that I can't be bothered to deal with, so enjoy that at 200 px")
        length=200
    if length < 50:
        print("Have you considered that length's too small? I drew it at 200 px instead")
        length=200
    x=int(input("What's your starting point's x-coordinate? "))
    if x > 400 or x < -400:
        print("That value is too dumb, I set it to 0")
        x=0
    y=int(input("What's the y coordinate? "))
    if y > 400 or y < -400:
        print("That value is too dumb, I set it to 0")
        y=0
    print("Your shape's done")
    pen.up()
    pen.setpos(x,y)
    pen.down()
    if sides > 2:
        angle=(180*(sides-2))/sides
    if sides==0:
        pen.circle(length)
    if sides > 2 and length <= 500 and length >= 50:
        for x in range(sides):
            pen.forward(length)
            pen.left(180-angle)
main()

turtle.update()
turtle.exitonclick()

