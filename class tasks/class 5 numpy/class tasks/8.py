# Example 12: NumPy - Boolean Indexing

import numpy as np

array = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(array[array % 2 == 0])