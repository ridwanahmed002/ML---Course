# Example 7: Tuple Comprehension (using generator expression)
# Tuples do not support comprehension like lists.
# However, you can use a generator expression to create a tuple.

squares = tuple(x**2 for x in range(10))
print(squares)