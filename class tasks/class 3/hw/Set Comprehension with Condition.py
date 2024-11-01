#Set Comprehension with Condition

#set comprehension means that you can create a set with a condition

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

squares = {x**2 for x in numbers if x % 2 == 0}
print(squares)

even_numbers = {x for x in numbers if x % 2 == 0}
print(even_numbers)