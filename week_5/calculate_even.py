def count_even(numbers):
    count = 0
    for number in numbers:
        if number % 2 == 0:
            count += 1
    return count


mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = count_even(mylist)
print(f"The number of even numbers in my list is {result}")

