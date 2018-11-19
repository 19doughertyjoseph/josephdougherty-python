import turtle as t


def main():
    t.setup(width=800 , height=800)
    t.title("Turtle Project")
    t.bgcolor("#1de047")
    t.hideturtle()
    t.speed(0)
    quadOne()
    quadFour()
    quadThree()
    quadTwo()
    t.exitonclick ()


def quadOne():
    movePoint(150,250)
    t.pencolor('red')
    for x in range(0,4) :
        t.forward(90)
        t.right(90)


def quadFour():
    movePoint(150,-250)
    t.pencolor('purple')
    t.forward(100)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(50)


def quadThree():
    movePoint(-150,-150)
    t.pencolor('blue')
    t.circle(50)


def quadTwo():
    movePoint(-150,150)
    t.pencolor('pink')
    t.left(45)
    t.forward(100)
    t.left(120)
    t.forward(100)
    t.left(120)
    t.forward(100)


def movePoint(x , y):
    t.penup ()
    t.setpos(x , y)
    t.pendown ()


main()
