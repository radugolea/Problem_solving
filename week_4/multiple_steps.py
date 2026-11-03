def display_ladder():
        print("""| |
***""")


def create_ladder(steps):
    steps=input("Enter number of steps:\n ")
    for i in range(int(steps)):
        display_ladder()

create_ladder(0)

