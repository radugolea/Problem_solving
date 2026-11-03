
def reverse_find_ascii():
    print("Program Started!")
    code = abs(int(input("Enter an ASCII code:\n ")))
    character = chr(code)
    if code in range(32,127):
        print(f"The character represented by ASCII code {code} is: {character}")
        print("Program Ended!")
    else:
        print("Code needs to be between 32 and 126 ")

reverse_find_ascii()