import time
from Snek import *
from turtle import Turtle, Screen

snek = Snek()
screen.tracer(0)

game_is_on = True
screen.update()
while game_is_on:
    screen.update()
    time.sleep(0.1)
    screen.listen()
    screen.onkey(key="d", fun=snek.move_right)
    screen.onkey(key="a", fun=snek.move_left)
    screen.onkey(key="w", fun=snek.move_up)
    screen.onkey(key="s", fun=snek.move_down)
    snek.move()


screen.exitonclick()