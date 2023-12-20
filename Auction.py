from replit import clear
#HINT: You can call clear() to clear the output in the console.
bid = {}
def bidding():

  print("What is your name:")
  name = input()
  print("What is your bid:")
  bid_price = int(input())

  bid[name] = bid_price

  print("Are there any other bidders ?")
  another = input()

  if another == "yes":
    clear()
    bidding()
  else:
    winner_bid = max(bid, key=bid.get)
    winner_value = max(bid.values())
    print(f"The winner is {winner_bid} with a bid of {winner_value}")

bidding()