def turn_right():
    turn_left()
    turn_left()
    turn_left()

# delete one move() at top of jump()
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()

