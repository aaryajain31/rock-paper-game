import random

print("choose option rock paper scissors")

user = input("enter choice: ").lower()
options = ["rock", "paper", "scissors"]

computer = random.choice(options)

print("you choose", user)
print("computer choose", computer)

if user == computer:
    print("tie")

elif user == "rock" and computer == "scissors": 
    print("you win")

elif user == "paper" and computer == "rock": 
    print("you win")

elif user == "scissors" and computer == "paper": 
    print("you win")
    
else:
    print("you lose")