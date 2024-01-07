from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)
def move_clockwise():
    tim.right(30)

def move_anticlockwise():
    tim.left(30)
def clear():
    tim.clear()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="a", fun=move_anticlockwise)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
