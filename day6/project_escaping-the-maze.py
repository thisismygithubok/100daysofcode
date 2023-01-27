#Maze from reeborg.ca - DID NOT GET THIS AT ALL, SO COMPLICATED, DID NOT UNDERSTAND THE LOGIC

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear():
    move()
turn_left()


while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()