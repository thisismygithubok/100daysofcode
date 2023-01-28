#Hangman Step 1
import random
from art import stages,logo #Import stages and logo from art.py
from dictionary import word_list #Import word_list from dictionary.py
import os #Importing to be able to clear screen after each guess

# word_list = ["Australia","Germany","Cameroon"] #Debug - set local word list
chosen_word = random.choice(word_list).lower() #Randomly choose a word from the word list
len_chosen_word = len(chosen_word) #Grab the length of the randomly chosen word
display = [] #Create blank list to add to for the display output
player_lives = len(stages)-1 #Variable to dynamically determine the number of lives, if someone wants to add more stages (body parts) that can be lost

for _ in range(len_chosen_word): #Adding a "_" to the display list for however many chars are in the randomly chosen word
    display += "_"
#print(display) #Debug - printing out the display to see if it properly created it
print(logo)
# print("The word is: "+chosen_word) #Debug - printing out that randomly chosen word

end_of_game = False #Setting current end of game status to false

while not end_of_game: #While loop to run through while end of game still = false
    guess = input("\nGuess a letter: ").lower() #Take user guess input as guess
    os.system("clear") #Running clear command to keep only most recent guess on screen
    if guess in display:
      print("You've already guessed: "+guess+"!") #Print out the user guess if they've already guessed that letter and it was right
    for position in range(len_chosen_word): #For each position in range of the length of chosen_word
        letter = chosen_word[position] # Setting letter = the current run through (position) in chosen_word
        if letter == guess: #If that current position's letter = the user's guessed letter
            #print(True) #Debug - prints out if that letter matches with any positions
            display[position] = letter #Replace the display's "_" with the matched position's letter
    if guess not in chosen_word: 
        player_lives -= 1 #Remove one life from remaining lives if guess is wrong
        print("You've guessed wrong!")
        print(stages[player_lives]) #Print the stage associated with lives remaining
        if player_lives == 0:
            end_of_game = True #If player hits 0 lives, end of game is now true
            print("Oh no, you've lost!")
    if guess in chosen_word:
        print(stages[player_lives]) #If player guess is correct, print the stage associated with lives remaining
            #print(False) #Debug - prints out if that letter does NOT match with any position
    print(f"{' '.join(display)}") #Print out the current list including all guesses using join
    if "_" not in display:
        end_of_game = True #Once all letters have been guessed correctly, the end of game is now true with a win!
        print("You've won!")