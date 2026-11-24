#create a file
filename = "words.txt"
#open and write in it
with open(filename, "w", encoding="utf-8") as f:
    f.write("This is a file im trying to open with python and count words\n")
    f.write("It also has a search function on lower case words\n")
#read file
with open(filename, "r", encoding="utf-8") as f:
    text = f.read().lower()
    print(text)
#split the text and count the words
words = text.split()
total_words = len(words)
print(words)
print(total_words)

#count the characters
characters = len(text)
print(characters)

user_input = input("Enter a word: ")
if user_input in words:
    print("Found!")
else:
    print("Not found!")