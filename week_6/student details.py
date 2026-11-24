student_details = "Students.txt"
with open(student_details, "w", encoding="utf-8") as file:
    file.write("John\nMary\nDavid\n")
7
with open(student_details, "r", encoding="utf-8") as file:
    text = file.read()
    print(text)

with open(student_details, "w", encoding="utf-8") as file:
    new_text = text.replace("Mary","Sarah")
print(new_text)
print("Student details updated")
