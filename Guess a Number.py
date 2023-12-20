# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random


def play(x, n):
    print("Guess: ")
    guess = int(input())
    if n == 1:
        print("You lose")
        exit()

    if guess == x:
        print("Yeay you got it right!")
    elif guess < x:
        print("Too low")
        n -= 1
        print("You have " + str(n) + " attempts left")
        play(x, n)
    elif guess > x:
        print("Too High")
        n -= 1
        print("You have " + str(n) + " attempts left")
        play(x, n)


num = 0
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
target = random.randint(0, 101)
print("Choose a difficulty. Type 'easy' or 'hard':")
difficulty = input()

if difficulty == "easy":
    num = 10
    print("You have 10 attempts to guess")
elif difficulty == "hard":
    num = 5
    print("You have 5 attempts to guess")

play(target, num)
