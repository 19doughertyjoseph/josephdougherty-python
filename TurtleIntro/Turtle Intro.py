import turtle

turtle.setup(width=500, height=500)
pen = turtle.Pen()


black_color = (0.0, 0.0, 0.0)
white_color = (1.0, 1.0, 1.0)
red_color = (1.0, 0.0, 0.0)
green_color = (0.0, 1.0, 0.0)
blue_color = (0.0, 0.0, 1.0)

turtle.bgcolor(red_color)



def squareDrawing(angle):
    moveTo(-100, -50)
    for x in range(4):
        pen.pencolor(black_color)
        pen.forward(40)
        pen.left(angle)



def rectangleDrawing(angle):
    moveTo(100, 50)
    for x in range(2):
        pen.pencolor(blue_color)
        pen.forward(40)
        pen.left(angle)
        pen.forward(80)
        pen.left(angle)


def squareDrawing2(angle):
    moveTo(-100, 50)
    for x in range(4):
        pen.pencolor(white_color)
        pen.forward(40)
        pen.left(angle)


def rectangleDrawing2(angle):
    moveTo(100, -50)
    for x in range(2):
        pen.pencolor(green_color)
        pen.forward(40)
        pen.left(angle)
        pen.forward(80)
        pen.left(angle)



def moveTo(x, y):
    pen.penup()
    pen.setpos(x, y)
    pen.pendown()



squareDrawing(90)
rectangleDrawing(90)
squareDrawing2(90)
rectangleDrawing2(90)


turtle.exitonclick()
