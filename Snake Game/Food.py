from turtle import Turtle, Screen
from random import randint

class Food:

    def __init__(self):
        self.segments = []
        self.create_food()

    def create_food(self):
        x_food = randint(1, 600)
        y_food = randint(1, 600)
        new_food = Turtle(shape="circle")
        new_food.goto(x_food,y_food)