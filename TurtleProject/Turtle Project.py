import turtle

turtle.setup(width=750, height=750)

pen = turtle.Pen()
pen.speed(200)

black_color = (0.0, 0.0, 0.0)
white_color = (1.0, 1.0, 1.0)
red_color = (1.0, 0.0, 0.0)
green_color = (0.0, 1.0, 0.0)
blue_color = (0.0, 0.0, 1.0)


def basicLine():
    moveTo(-50, 0)
    pen.forward(100)

#The origin on the screen is (0,0)

def basicSquare():
    pen.pencolor(blue_color)
    moveTo(-100, -100)
    for x in range(4):
        pen.forward(200)
        pen.left(90)


def basicCircle():
    pen.pencolor(red_color)
    moveTo(0, -300)
    pen.circle(300)

def basicTriangle():
    pen.pencolor('#33cc8c')
    moveTo(-200, -150)
    for x in range(3):
        pen.forward(400)
        pen.left(120)



def moveTo(x, y):
    pen.penup()
    pen.setpos(x, y)
    pen.pendown()

#Between drawings we have to pick up the pen and move it to the desired location

basicLine()
basicSquare()
basicCircle()
basicTriangle()

turtle.exitonclick()
