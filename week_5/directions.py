def directions():
    steps=["Move Forward", "Move Backward", "turn left", "turn right"]
    return steps
def menu():
    select=directions()
    print("Please select a direction:\n")
    for index in range(len(select)):
        print(f"{index}. {select[index]}")
def run_task3():
    menu()
run_task3()