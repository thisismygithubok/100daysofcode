#Banker Roulette
# Import the random module here

import random

# Split string method

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

# 🚨 Don't change the code above 👆

#Write your code below this line 👇

num_names = len(names) #This counts how many names there are, 5
random_name = random.randint(0, num_names - 1) #This tells it to grab a random number from the list of names, with 0 being the 1st name, and (num_names - 1) 4 being the 5th name
select_name = names[random_name] #This pulls the random name by having the random # be the position of the name from the list to select.

print(select_name+" is going to buy the meal today!") #This prints out that randomly selected name.