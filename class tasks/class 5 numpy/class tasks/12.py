# Example 28: NumPy - Conditional Replacement with np.where

import numpy as np

array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

result = np.where(array % 2 == 0, -1, array)
print(result) # [ 1 -1  3 -1  5 -1  7 -1  9 -1]