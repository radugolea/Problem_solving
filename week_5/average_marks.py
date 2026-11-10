def average_marks(marks):
    average= sum(marks) / len(marks)
    return average

#mylist=[23,65,100,41]
mylist= list(map(int, input("Enter the marks separated by space: ").split()))
result = average_marks(mylist)
print(f"Average marks ot of 100 is {result} %")
