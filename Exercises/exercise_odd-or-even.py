#Checking if number is odd or even

number = int(input("Which number do you want to check? : "))

divided_result = number % 2

if divided_result == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")