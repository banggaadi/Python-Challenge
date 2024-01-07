from turtle import Turtle, Screen
from random import randint

def initialize_turtle(color, y_position):
    turtle = Turtle()
    turtle.color(color)
    turtle.speed("fastest")
    turtle.shape("turtle")
    turtle.penup()
    turtle.setpos(-400, y_position)
    return turtle

def race(turtles, finish_line):
    while True:
        for turtle in turtles:
            turtle.forward(randint(10, 20))
            if turtle.pos()[0] >= finish_line:
                return turtle  # Return the winning turtle

def announce_winner(winning_turtle):
    print(f"The {winning_turtle.color()[0]} turtle wins!")

def main():
    screen = Screen()

    colors = ["red", "blue", "green"]
    turtles = [initialize_turtle(color, index * 40) for index, color in enumerate(colors)]

    finish_line = 400

    answer = screen.textinput("Make your bet", "Who will win the race? Choose a color").lower()
    if answer is None:
        print("Goodbye!")
        screen.bye()
        return

    print("Start!")

    winning_turtle = race(turtles, finish_line)
    print("FINISH")

    announce_winner(winning_turtle)

    if answer == winning_turtle.color()[0].lower():
        print("Congratulations! You won the bet!")
    else:
        print("Sorry, you lost the bet.")

    screen.exitonclick()

if __name__ == "__main__":
    main()
