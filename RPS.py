import random 

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

print("Choose: rock, paper, scissors")
user = input("Enter choice: ").lower()

options = ["rock", "paper", "scissors"]
computer = random.choice(options)

print("\nYou chose:")
if user == "rock":
    print(rock)
elif user == "paper":
    print(paper)
elif user == "scissors":
    print(scissors)
else:
    print("Invalid input")

print("Computer chose:")
if computer == "rock":
    print(rock)
elif computer == "paper":
    print(paper)
elif computer == "scissors":
    print(scissors)

# Game logic
if user == computer:
    print("It's a tie!")
elif user == "rock" and computer == "scissors":
    print("You win! Rock crushes scissors ")
elif user == "paper" and computer == "rock":
    print("You win! Paper covers rock ")
elif user == "scissors" and computer == "paper":
    print("You win! Scissors cut paper ")
else:
    print("You lose ")

