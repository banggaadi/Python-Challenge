from game_data import data
import random

final_score = 0


def check(answer, A, B):
    global final_score
    if answer == "A" and A["follower_count"] > B["follower_count"]:
        print("You're Right")
        final_score += 1
        print("Your Score:", final_score)
        print("\n")
        play()
    elif answer == "B" and A["follower_count"] < B["follower_count"]:
        print("You're Right")
        final_score += 1
        print("Your Score:", final_score)
        print("\n")
        play()
    else:
        print("You are wrong, this is your final score:", final_score)


def play():
    first_option = random.choice(data)
    second_option = random.choice(data)

    print("Compare\nA= " + first_option["name"] + ", a " + first_option["description"] + ", from " + first_option[
        "country"] + "\n VS \nB= " + second_option["name"] + ", a " + second_option["description"] + ", from " +
          second_option["country"])
    print("Who has more followers?")

    answer = input()
    check(answer, first_option, second_option)


play()


