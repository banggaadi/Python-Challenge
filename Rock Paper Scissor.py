from random import randint
def play(x, y):
  rps = ["rock", "paper", "scissor"]
  if x == y:
    print(f"{rps[x]} vs {rps[y]} Draw")
  elif x == 0 and y == 1:
    print(f"{rps[x]} vs {rps[y]} You lose")
  elif x == 0 and y == 2:
    print(f"{rps[x]} vs {rps[y]} You win")
  elif x == 1 and y == 2:
    print(f"{rps[x]} vs {rps[y]} You lose")
  elif x == 1 and y == 0:
    print(f"{rps[x]} vs {rps[y]} You win")
  elif x == 2 and y == 0:
    print(f"{rps[x]} vs {rps[y]} You lose")
  elif x == 2 and y == 1:
    print(f"{rps[x]} vs {rps[y]} You win")



  
print("Welcome to Rock, Paper, Scissors!")

print("Choose 0 for rock, 1 for paper, or 2 for scissors:")
move = int(input())
opp_move = randint(0,2)
play(move, opp_move)
