#Logical Operators

#AND, OR, NOT
#AND - both have to be true
#OR - only one has to be true
#NOT - reverse the boolean value, i.e. true becomes false, or false becomes true

height = int(input("How tall are you in cm? : ")) #Input on how tall the user is in cm
bill = 0 #base level bill owed

if height >= 120: #If user is 120cm or taller, go to next condition, age.
    print("You can ride the rollercoaster!")
    age = int(input("How old are you? : ")) #Age input if user is 120cm or taller

    if age < 12: #If user is less than 12yo
        bill = 5
        print("Child tickets are $5")
    elif age <=18: #If user is older than 12, but only 13-18yo
        bill = 7
        print("Youth tickets are $7")
    elif age >=45 and age <= 55: #If user is between 45 and 55
        print("Your ticket is free!")
    else: #If user is 19-44 or 56-infinity
        bill = 12
        print("Adult tickets are $12")

    want_photo = input("Do you want a photo taken? y or n ")
    if want_photo == "y":
        #Add $3 to bill
        bill += 3
    
    print(f"Your total is: ${bill}")

else: #Condition only met if user is less than 120cm tall
    print("Sorry, you need to be taller to ride the rollercoaster :(")