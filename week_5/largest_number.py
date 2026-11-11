def largest_number(numbers):
    largest=max(numbers)
    return largest

def smallest(numbers):
    smallest=min(numbers)
    return smallest

mylist=[12,22,31,212,331]
result = largest_number(mylist)
result1 = smallest(mylist)
print(f"the largest number in my list is {result}")
print(f"the smallest in my list is {result1}")