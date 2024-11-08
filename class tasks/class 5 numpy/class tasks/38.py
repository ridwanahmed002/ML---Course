# Example 13: NumPy - Indexing Multi-dimensional Arrays with Slices

import numpy as np

array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(array[0:2, 1:3]) # [[2 3] [5 6]]


# array[0:2, 1:3] selects the first two rows (index 0 and 1) and the second and third columns (index 1 and 2), creating a subarray with the values: [[2 3] [5 6]]