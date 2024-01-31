from turtle import Turtle, Screen

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snek")
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snek:
    def __init__(self):
        self.segments = []
        self.create_snek()
        self.head = self.segments[0]

    def create_snek(self):
        for position in STARTING_POSITION:
            new_snek = Turtle(shape="square")
            new_snek.penup()
            new_snek.color("white")
            new_snek.goto(position)
            self.segments.append(new_snek)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)

        self.head.forward(20)
