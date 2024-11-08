# Example 22: NumPy - Extract Lower Triangle of a Matrix

import numpy as np

array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

lower_triangle = np.tril(array)
print(lower_triangle)