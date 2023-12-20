from game_data import data
import random

final_score = 0
game_should_continue = True


def get_option():
    return random.choice(data)


def check(answer, A, B):
    global final_score
    global game_should_continue
    if answer == "A" and A["follower_count"] > B["follower_count"]:
        print("You're Right")
        final_score += 1
        print("Your Score:", final_score)
        print("\n")
        return A
    elif answer == "B" and A["follower_count"] < B["follower_count"]:
        print("You're Right")
        final_score += 1
        print("Your Score:", final_score)
        print("\n")
        return B
    else:
        print("You are wrong, this is your final score:", final_score)
        game_should_continue = False
        return None


def play():
    global game_should_continue
    global final_score

    first_option = get_option()
    second_option = get_option()

    while game_should_continue:
        print("Compare\nA= " + first_option["name"] + ", a " + first_option["description"] + ", from " +
              first_option["country"] + "\n VS \nB= " + second_option["name"] + ", a " + second_option["description"] +
              ", from " + second_option["country"])
        print("Who has more followers?")

        answer = input()
        new_first_option = check(answer, first_option, second_option)

        if game_should_continue:
            if new_first_option:
                first_option = new_first_option
                second_option = get_option()


play()

