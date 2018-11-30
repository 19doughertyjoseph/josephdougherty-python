import turtle as t

import turtle as t


def main () :
    t.setup(width=800 , height=800)
    t.title("Rosette")
    t.bgcolor("red")
    t.hideturtle()
    t.speed(0)
    rosette()
    spiral()
    t.exitonclick()

def rosette ():
    t.pensize(0.1)
    for x in range(80):
        t.pencolor('white')
        t.circle(200)
        t.left(80)


def spiral():
    spiral = t.Turtle()
    t.width(10)
    for i in range(90):
        spiral.forward(i * 10)
        spiral.right(144)


main()
