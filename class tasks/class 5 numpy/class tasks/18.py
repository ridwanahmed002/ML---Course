# Example 12: NumPy - Combining Boolean and Fancy Indexing

import numpy as np

array = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(array[array % 2 == 0])
print(array[array > 2])

result = array[(array > 4) & (array < 9)][[0, 2]]
print(result) # [5, 7]