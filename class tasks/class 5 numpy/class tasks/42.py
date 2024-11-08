# Example 14: NumPy - Unique Elements and Counting

import numpy as np

array = np.array([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])

unique, counts = np.unique(array, return_counts=True)
print(unique) # [1 2 3 4]
print(counts) # [1 3 4 5]