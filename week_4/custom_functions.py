def listen():
    word=input("What sound did you hear?\n")
    if word == "rumble" or word == "thunder":
        print(f"That was a loud {word}!")
    else:
        print(f"What was that?")
        word_2 = input("Please type again\n")
        print(f"Ahhh you meant {word_2}")

listen()