
def find_ascii():
    print("Program Started!")
    letter = input("Enter a letter:\n ")
    value_letter = ord(letter)
    if len(letter) >1:
        print("Letter can only contain one letter")
    else:
        print(f"The ASCII code for {letter} is: {value_letter}")
        print("Program Ended!")
find_ascii()