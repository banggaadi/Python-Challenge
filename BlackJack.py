import random

def check(dealer_cards, user_cards):
  if sum(dealer_cards) == 21 and sum(user_cards) == 21:
    print("Draw")
    exit()
  elif sum(dealer_cards) == 21:
    print("Dealer won")
    exit()
  elif sum(user_cards) == 21:
    print("You Win")
    exit()


def play(dealer_cards, user_cards):
  print("Hit ?")
  answer = input()
  if answer == "yes":
    user_hit(user_cards)
  else:
    dealer_hit(dealer_cards, user_cards)

def user_hit(user_cards):
  add = random.sample(cards, 1)
  user_cards.extend(add)
  if 11 in user_cards and sum(user_cards) > 21:
    user_cards.remove(11)
    user_cards.extend(1)
  print(f"Hit card is: {add} your total is {sum(user_cards)}")
  if sum(user_cards) > 21:
    print("Bust ! you lose")
    exit()
  play(dealer_cards, user_cards)

def dealer_hit(dealer_cards, user_cards):
  if 11 in dealer_cards and sum(dealer_cards) > 21:
    dealer_cards.remove(11)
    dealer_cards.extend(1)
  if sum(dealer_cards) > sum(user_cards):
      print("You lose")
  else:
      add = random.sample(cards, 1)
      dealer_cards.extend(add)
      print(f"Hit card is: {add} Dealer's total is {sum(dealer_cards)}")
      if sum(dealer_cards) < 21:
        dealer_hit(dealer_cards, user_cards)
      elif sum(dealer_cards) > 21:
        print("Bust ! you win")
        exit()


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
dealer_cards = []
user_cards = []
print("Welcome to BlackJacks")
print("Do you want to play ? type 'yes' or 'no'")

answer = input()
dealer_cards = random.sample(cards, 2)
user_cards = random.sample(cards, 2)
print("Dealer Cards = ",dealer_cards)
print("User Cards = ",user_cards)
print(f"Dealer's cards:{sum(dealer_cards)}\nYour cards:{sum(user_cards)}")
check(dealer_cards, user_cards)

if answer == "yes":
  play(dealer_cards, user_cards)
else:
  exit()
