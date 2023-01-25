#Multiple if statements in succession

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
    elif age < 65: #If user is 19-64
        bill = 12
        print("Adult tickets are $12")
    else: #If user is 65 or older
        print("Your ticket is free!")

    want_photo = input("Do you want a photo taken? y or n ")
    if want_photo == "y":
        #Add $3 to bill
        bill += 3
    
    print(f"Your total is: ${bill}")

else: #Condition only met if user is less than 120cm tall
    print("Sorry, you need to be taller to ride the rollercoaster :(")