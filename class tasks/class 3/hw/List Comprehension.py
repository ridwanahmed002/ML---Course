# Example 8: List Comprehension with Conditional Nesting

# Using list comprehension with nested loops and conditions to filter elements.

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
filtered_matrix = [[num for num in row if num % 2 == 0] for row in matrix] #here what we are doing is filtering out the odd numbers

print(filtered_matrix)