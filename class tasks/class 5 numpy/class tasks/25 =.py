# Example 24: NumPy - Indexing with np.take

import numpy as np

array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

result = np.take(array, [0, 2])
print(result) # [1 3]

#np.take(array, [0, 2]) will select elements at indices 0 and 2 in this flattened version, giving: [1, 3]