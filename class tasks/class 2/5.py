# Example 5: Removing Key-Value Pairs from a Dictionary

# You can remove key-value pairs using the pop() method, which removes the specified key and returns its value.
# The del keyword can also be used to remove a specific key or clear() to remove all items.

my_dict = {"name":"Arman","age":24,"address":"Kathmandu"}
removed_value = my_dict.pop("city")
print(removed_value)
print(my_dict)