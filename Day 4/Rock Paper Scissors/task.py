import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
fight = [rock, paper, scissors]
choices = ["rock", "paper", "scissors"]

userChoice = input("Rock, Paper, or Scissors? \n").lower()

if userChoice in choices:
    userIndex = choices.index(userChoice)
    computerIndex = random.randint(0, 2)

    print(f"\nYou chose:\n{fight[userIndex]}")
    print(f"Computer chose:\n{fight[computerIndex]}")

    if userIndex == computerIndex:
        print("It's a draw!")
    elif (userIndex == 0 and computerIndex == 2) or \
         (userIndex == 1 and computerIndex == 0) or \
         (userIndex == 2 and computerIndex == 1):
        print("You win!")
    else:
        print("You lose!")
else:
    print("Invalid choice. Please choose Rock, Paper, or Scissors.")