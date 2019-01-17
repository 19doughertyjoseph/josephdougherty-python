import turtle as t


def main () :
    t.setup(width=800 , height=800)
    t.title("Rosette")
    t.bgcolor("blue")
    t.hideturtle()
    t.speed(0)
    backGround()
    t.exitonclick()


def backGround ():
    t.pensize(0.1)
    for x in range(80):
        t.pencolor('red')
        t.width(20)
        t.circle(200)
        t.left(80)

    for x in range(90):
        t.pencolor('yellow')
        t.width(5)
        t.circle(150)
        t.left(4)

    for x in range(180):
        t.pencolor('black')
        t.width(10)
        t.circle(100)
        t.left(80)



main()
