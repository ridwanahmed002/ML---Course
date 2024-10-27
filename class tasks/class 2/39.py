# Example 9: Sorting a Tuple

# Tuples are immutable and cannot be sorted directly.
# To sort a tuple, you need to convert it to a list, sort it, and convert it back to a tuple.

my_tuple = (2,9,7,4,12)
sorted_tuple = tuple(sorted(my_tuple))
print(sorted_tuple)