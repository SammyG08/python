"""
import random

gameOptions = ("rock","paper","scisssors")

firstPlayer = random.choice(gameOptions)
secondPlayer = random.choice(gameOptions)
print(firstPlayer,"and",secondPlayer)

if firstPlayer == "rock" and secondPlayer != "rock" or "paper":
    print(f"{firstPlayer} won this round\n.")

elif firstPlayer == "paper" and secondPlayer != "paper" or "scissors":
    print(f"{firstPlayer} won this round.\n")
    
elif firstPlayer == "scissors" and secondPlayer != "rock" or "scissors":
    print(f"{firstPlayer} won this round.\n")
    
elif firstPlayer == "rock" and secondPlayer == "paper":
    print(f"{secondPlayer} won this round\n.")
    
elif firstPlayer == "paper" and secondPlayer == "scissors":
    print(f"{secondPlayer} won this round\n.")
    
elif firstPlayer == "scissors" and secondPlayer == "rock":
    print(f"{secondPlayer} won this round\n.")
   
else :
    print("It was a tied round")
"""

