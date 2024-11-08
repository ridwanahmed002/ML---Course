# Example 4: NumPy - Fancy Indexing

import numpy as np

array = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(array[[0, 1], [2, 3]]) #[3 9]

# Here, [0, 1] specifies the rows and [2, 3] specifies the columns.

# The first element in the result is determined by the first pair of indices: row 0 and column 2.
# array[0, 2] is 3.
# The second element in the result is determined by the second pair of indices: row 1 and column 3.
# array[1, 3] is 9.