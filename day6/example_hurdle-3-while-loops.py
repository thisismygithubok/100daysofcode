##Example from hurdles 3 from reeborg.ca

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def hurdle():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if front_is_clear():
        move()
    elif wall_in_front():
        hurdle()