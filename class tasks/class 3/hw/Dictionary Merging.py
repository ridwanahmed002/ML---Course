# Example 4: Dictionary Merging with Comprehension

# You can merge two dictionaries using a dictionary comprehension.

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

merged_dict = {**dict1, **dict2} #here ** is used to unpack dict1 and dict2
print(merged_dict)
