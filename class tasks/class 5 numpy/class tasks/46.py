# Example 16: NumPy - Splitting Arrays

import numpy as np  

array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(np.split(array, 2)) # [array([1, 2, 3, 4, 5]), array([6, 7, 8, 9, 10])]