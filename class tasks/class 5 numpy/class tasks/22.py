# Example 15: NumPy - Masked Indexing

import numpy as np

array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
mask =  array % 2 == 0
print(array[mask]) #[ 2  4  6  8 10]