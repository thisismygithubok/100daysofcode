#Treasure Island

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

choice1 = input("You're at a cross road. Where do you want to go? Type 'north', 'east', 'south', or 'west'.\n").lower()

if choice1 == "north":
    choice2 = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n").lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which color do you choose?\n").lower()
        if choice3 == "red":
            print("It's a room full of fire, game over.")
        elif choice3 == "yellow":
            print("You found the treasure, you win!")
        else: 
            print("You enter a room full of beasts, game over.")
    else: 
        print("You get attacked by an angry trout, game over.")
elif choice1 == "east":
    choice2 = input("You come to an abandoned mine shaft, do you want to enter? Yes or no.\n").lower()
    if choice2 == "yes":
        choice3 = input("You descend into the mineshaft, stumbling upon a 3-way intersection, do you want to go left, straight, or right?\n").lower()
        if choice3 == "left":
            choice4 = input("You wander for 3 hours before somehow finding your way back to the 3-way intersection, which way do you want to try now, straight or right?\n").lower()
            if choice4 == "straight":
                print("You suddenly experience a cavein and die, oh no! Game over.'?\n")
                exit()
        elif choice3 == "straight":
            print("You suddenly experience a cavein and die, oh no! Game over.'?\n")
            exit()
        else:
            choice5 = input("You find a door at the end which leads you up a ladder to an island!\n").lower()
            #This should loop back to the island section of north
    elif choice2 == "no":
        print("You decide to turn around and head back, the mine giving you the heebie jeebies.\n")
        #This should loop back to the island section of north
elif choice1 == "south":
    choice2 = input("You find yourself at the edge of a forest with 2 paths. Left has a wearly looking traveller beckoning for your assistance. Right has a seemingly clear router ahead, which do you choose?\n").lower()
    if choice2 == "left":
        choice3 = input("The weary traveller seems off, do you mug him, or run past him?\n").lower()
        if choice3 == "mug him":
            print("The weary travller brandishes a knife and stabs you, leaving you to bleed out, game over.")
        else:
            choice4 = input("You run past the weary travller after feeling uneasy about his presence and make your way to the far edge of the forest.\n").lower()
            #This should loop back to the island section of north
else:
    print("You fell into a hole, game over.")
