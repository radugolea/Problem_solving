def climb_ladder(steps,ladder):
    steps_left = steps - ladder
    if steps_left < ladder:
        print("Still some way to go!")
    else:
        print("We are almost there")

climb_ladder(5,2)
climb_ladder(2,5)