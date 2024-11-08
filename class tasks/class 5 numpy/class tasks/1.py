import numpy as np

array = np.array([[1,2,3],[5,6,7]])
first_row = array[0, :]
third_column = array[:, 2]

print(f"element at {1,3} is ;{array[1,2]}")
print(f"first row is {first_row}")
print(f"third column is {third_column}")