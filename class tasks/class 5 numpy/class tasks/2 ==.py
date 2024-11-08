import numpy as np

array_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
first_row = array_3d[0, :, :]
third_column = array_3d[:, :, 2]

print(f"first row is {first_row}")
print(f"third column is {third_column}")