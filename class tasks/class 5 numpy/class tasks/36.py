# Example 23: NumPy - Multi-dimensional Array Indexing with Mixed Types

import numpy as np

array_3d = np.array([[[1, 2], [3, 4]], 
                     [[5, 6], [7, 8]], 
                     [[9, 10], [11, 12]]])

print(array_3d[1, 0, 0]) # 5
print(array_3d[1, 1, 1]) # 8
print(array_3d[2, 0, 1]) # 10