# Example 2: Accessing Dictionary Values

# Values in a dictionary are accessed using their keys.
# If a key is not found, a KeyError will be raised unless you use the get() method, which returns None.
my_dict = {"name":"Arman","age":24,"address":"Kathmandu"}

name = my_dict["name"]
print(name)

age = my_dict.get("age", 25)
print(age)

age2 = my_dict["age"]
print(age2)