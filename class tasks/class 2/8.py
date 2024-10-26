# Example 8: Iterating Over a Dictionary

# You can iterate over a dictionary to access its keys, values, or key-value pairs.

my_dict = {"name":"Arman","age":24,"address":"Kathmandu"}
for key in my_dict:
    print(key, my_dict[key])

for key, value in my_dict.items():
    print(key, value)