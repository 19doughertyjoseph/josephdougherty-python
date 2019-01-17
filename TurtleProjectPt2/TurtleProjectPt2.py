import turtle


def main():
    turtle.setup(width=800 , height=800)
    turtle.title("Turtle Graphics - turtleIntro")
    turtle.bgcolor("#1de047")
    turtle.hideturtle()
    turtle.speed(0)
    inputinfo ()
    circle ()
    turtle.exitonclick ()

def inputinfo () :
    color = input ('Input a color to draw with - ')
    length = int(input('Input the length in pixels of each side - '))
    number = int(input('Input the number of sides for your polygon - '))
    if number <= 2 :
        wrong()
    something (color , length , number)


def something (c, l, n) :
    turtle.pencolor(c)
    turtle.penup()
    b = (l / -2)
    c = (l / 2)
    turtle.setpos(b , c)
    turtle.pendown ()
    a = 360 / n
    for x in range(0,n) :
        turtle.forward(l)
        turtle. right(a)

def circle () :
    turtle.penup()
    turtle.setpos(-250,-250)
    turtle.pendown()
    turtle.circle(50)

def wrong () :
    p = input('Polygons must have 3 or more sides')

main ()
