# Example 8: NumPy - Conditional Indexing

import numpy as np

array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

array[array % 2 == 0] = -1  

print(array) # [ 1 -1  3 -1  5 -1  7 -1  9 -1]