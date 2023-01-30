#Write your code below this line 👇

def prime_checker(number):
    is_Prime = True #Setting is_Prime = true by default, before running anything in function
    for i in range(2,number-1): #For each number in the range between 2 and the user input - 1 (this checks division of 2 through n-1)
        if number % i == 0: #If that number % 2 through n-1 = 0, it means it can be divided by that number, so is_Prime is now FALSE
            is_Prime = False
    if is_Prime == True: #Setting is_Prime = TRUE if it did not meet the condition above
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
#n = int(input("Check this number: "))
n = int(input("Check this number: ")) #User input of number
prime_checker(number=n) #Print the result of the prime_checker function