#Leap Year Exercise

#Leap year conditions
#Wholly divisible by 4? Leap year!
    #Wholly divisible by 100? Not a leap year UNLESS
        #Wholly divisible by 400? Leap year!
#Not wholly divisible by 4? Not a leap year

year = int(input("What year do you want to check? : "))

div_4 = year % 4 #Is year fully divisible by 4? What is the remainder? If remainder is whole, leap year!, if remainder is not whole, not leap year.
div_100 = year % 100 #Is year fully divisible by 100? What is the remainder? If remainder is whole, not a leap year UNLESS year/400 IS whole
div_400 = year % 400 #Is year fully divisible by 4, 100, AND 400? Leap year!
if div_4 == 0:
    if div_100 == 0:
        if div_400 == 0:
            print("Leap year.")
        else:
            print("Not a leap year.")
    else:
        print("Leap year.")
else:
    print("Not a leap year.")

#From example, could be a bit more concise

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not a leap year.")
    else:
        print("Leap year.")
else:
    print("Not a leap year.")