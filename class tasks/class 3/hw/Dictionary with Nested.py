# Example 7: Dictionary with Nested Structures

my_dict = {"name":"Arman","age":24,
           "address":{"city":"Kathmandu","country":"Nepal"}}
print(my_dict)

city = my_dict["address"]["city"]
print(city)

#modyfying

my_dict["address"]["city"] = "Lalitpur"
print(my_dict)