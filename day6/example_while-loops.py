#While Loops

while something_is_true:
    #do this
    #then do this
    #then do this - loop back to beginning if condition is still true

#Example from hurdles 2 from reeborg.ca

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def hurdle():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    hurdle()

#For loops best when needing to do something with EACH item in the list

#While loops best for needing to do something until a condition is met