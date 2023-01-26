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

#Write your code below this line 👇

import random

options = [rock, paper, scissors] #This tells us the 3 options are the variables rock, paper, or scissors, assigning them a value of 0 through 2, and also storing the picture
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n")) #This allows the user to input 0, 1, or 2, and stores that value as an int
computer_choice = random.randint(0, 2) #This sets the computer choice to a random int value between 0 and 2

print("\nYou chose: "+options[user_choice]) #This prints out what option the user chose from the options list
print("\nComputer chose: "+options[computer_choice]) #This prints out what the computer randomly chose from the options list

if user_choice >=3 or user_choice <0:
    print("You typed an invalid number, you lose!")
elif user_choice == 0 and computer_choice == 0:
    print("Draw!")
elif user_choice == 0 and computer_choice == 1:
    print("Paper beats Rock, you lose!")
elif user_choice == 0 and computer_choice == 2:
    print("Rock beats Scissors, you win!")
elif user_choice == 1 and computer_choice == 0:
    print("Paper beats Rock, you win!")
elif user_choice == 1 and computer_choice == 1:
    print("Draw!")
elif user_choice == 1 and computer_choice == 2:
    print("Scissors beats Paper, you lose!")
elif user_choice == 2 and computer_choice == 0:
    print("Rocks beats Scissors, you lose!")
elif user_choice == 2 and computer_choice == 1:
    print("Scissors beats Paper, you win!")
elif user_choice == 2 and computer_choice == 2:
    print("Draw!")