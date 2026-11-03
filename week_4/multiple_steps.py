def display_ladder(steps):
    steps=input("How many steps remain?\n")

    for i in range(int(steps)):
        print("""| |
***""")

display_ladder(0)