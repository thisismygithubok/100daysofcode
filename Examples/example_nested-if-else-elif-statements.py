#Nested if/else and elif statements

#Nested if/else
height = int(input("How tall are you in cm? : "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("How old are you? : "))
    if age >= 18:
        print("Your ticket will be $12")
    else:
        print("Your ticket will be $7")
else:
    print("Sorry, you need to be taller to ride the rollercoaster :(")


#Elif statement
height_2 = int(input("How tall are you in cm? : ")) #Input on how tall the user is in cm

if height_2 >= 120: #If user is 120cm or taller, go to next condition, age.
    print("You can ride the rollercoaster!")
    age_2 = int(input("How old are you? : ")) #Age input if user is 120cm or taller
    if age_2 < 12: #If user is less than 12yo
        print("Your ticket is $5")
    elif age_2 <=18: #If user is older than 12, but only 13-18yo
        print("Your ticket is $7")
    elif age_2 < 65: #If user is 19-64
        print("Your ticket is $12")
    else: #If user is 65 or older
        print("Your ticket is free!")
else: #Condition only met if user is less than 120cm tall
    print("Sorry, you need to be taller to ride the rollercoaster :(")