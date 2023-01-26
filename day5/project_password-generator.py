#Random Password Generator
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

num_letters = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like?\n"))
num_numbers = int(input("How many numbers would you like?\n"))

int_letters = len(letters) #Count how many letters there are, 52
int_symbols = len(symbols) #Count how many symbols there are, 9
int_numbers = len(numbers) #Count how many numbers there are, 10
password_list = []
password = ""

for each in range(num_letters): #Iterate through however many numbers the user selects
    random_letters = random.randint(0,int_letters) #Select a random letter's int value
    letter_selection = letters[random_letters-1] #Tells it what letter to grab from the letter list based on the random letter # - 1 (without -1 would be out of range)
    password += letter_selection ##Append the selected letter into the password string
    password_list.append(letter_selection) #Append the selected letter into the password_list array

for each in range(num_symbols): #Iterate through however many numbers the user selects
    random_symbols = random.randint(0,int_symbols) #Select a random symbol's int value
    symbol_selection = symbols[random_symbols-1] #Tells it what symbol to grab from the symbol list based on the random symbol # - 1 (without -1 would be out of range)
    password += symbol_selection ##Append the selected letter into the password string
    password_list.append(symbol_selection) #Append the selected letter into the password_list array

for each in range(num_numbers): #Iterate through however many numbers the user selects
    random_numbers = random.randint(0,int_numbers) #Select a random number's int value
    number_selection = numbers[random_numbers-1] #Tells it what number to grab from the number list based on the random number # - 1 (without -1 would be out of range
    password += number_selection ##Append the selected letter into the password string
    password_list.append(number_selection) #Append the selected letter into the password_list array

# print(stored_letters)
# print(stored_symbols)
# print(stored_numbers)
print(f"Your unshuffled random password is: {password}") ##This is the simplified password, no random shuffling, does letters->symbols->nums - can't shuffle items in a string.

# print(password_list) ##Password in list pre-shuffle
random.shuffle(password_list) #Randomly shuffles a list
# print(password_list) ##Password in list post-shuffle

password_random = "" #Create random password string

for each in password_list: 
    password_random += each #For each item in the now shuffled password, add it into the string.

print(f"Your shuffled random password is: {password_random}") #Print the final jumbled password string.