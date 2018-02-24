import turtle

def Draw_Square(InitAngle):
    MyTurtle = turtle.Turtle()
    MyTurtle.shape("turtle")
    MyTurtle.color("blue")
    MyTurtle.right(InitAngle)
    MyTurtle.speed(20)
    for i in range(4):
        MyTurtle.forward(100)
        MyTurtle.right(90)


def Draw_circle_by_squares():

    angle = 10
    BckGround = turtle.Screen()
    BckGround.bgcolor("yellow")

    for i in range(36):
        Draw_Square(i*angle)
    BckGround.exitonclick()


Draw_circle_by_squares()

