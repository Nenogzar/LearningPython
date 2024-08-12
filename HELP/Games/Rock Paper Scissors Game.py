import random

while True:
    player1 = input("Select Rock, Paper, or Scissor: ").lower()
    if player1 == "rock" or player1 == "paper" or player1 == "scissor":
        break
    else:
        print("Wrong choice, try again.")

player2 = random.choice(["rock", "paper", "scissor"]).lower()
print("Player 1 selected:", player1)
print("Player 2 selected:", player2)

if player1 == player2:
    print("Tie")
elif (player1 == "rock" and player2 == "paper") or (player1 == "paper" and player2 == "scissor") or (player1 == "scissor" and player2 == "rock"):
    print("Player 2 Won")
else:
    print("Player 1 Won")
