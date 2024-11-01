my_list = [[1,2,3],[4,[5,6]],7,8]

nested_element = my_list[1][1][0]
print(f"Nested element is {nested_element}")

my_list[2] = 100
print(f"Updated list is {my_list}")

flattened_list = my_list[0] + my_list[1] + my_list[3:]
print(f"Flattened list is {flattened_list}")

flattened_list2 = my_list[0] + my_list[1]
print(f"Flattened list 2 is {flattened_list2}")