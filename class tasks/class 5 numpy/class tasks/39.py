# Example 10: NumPy - Modifying Array Values using Indexing

import numpy as np

array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

array[3:7] = 0

print(array) # [1 2 3 0 0 0 0 8 9 10]