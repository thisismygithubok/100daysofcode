#Functions

print("Hello")
num_char = len("Hello")
print(num_char)

#Making our own functions
def my_function():
    print("Hello")
    print("Bye")

my_function() #Calls our custom function

#Performed some more examples over at https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=%2Fworlds%2Fmenus%2Fselect_collection_en.json&name=Alone&url=%2Fworlds%2Ftutorial_en%2Falone.json

def turn_around():
    turn_left()
    turn_left()
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()

#Draw Square
turn_left()
move()
turn_right()
move()
turn_right()
move()
turn_right()
move()
turn_around()