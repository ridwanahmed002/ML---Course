# Example 30: NumPy - Combining Multiple Indexing Techniques

import numpy as np

array = np.array([[1, 2, 3, 4, 5], 
                  [6, 7, 8, 9, 10], 
                  [11, 12, 13, 14, 15]])

result = array[:, [0, 2]][array[:, [0, 2]] > 4]
print(result) # [ 6  8 11 13]

# array[:, [0, 2]]
# This code selects columns 0 and 2 from each row, creating a new 2D array:
# [[ 1,  3], 
#  [ 6,  8], 
#  [11, 13]]

# array[:, [0, 2]] > 4
# This creates a boolean array of the same shape as array[:, [0, 2]], where each element is True if it is greater than 4 and False otherwise:
# [[False, False], 
#  [ True,  True], 
#  [ True,  True]]

# array[:, [0, 2]][array[:, [0, 2]] > 4]
# Here, array[:, [0, 2]] > 4 is used as an index to select only the True values from array[:, [0, 2]]. This operation flattens the selected elements into a 1D array because numpy’s boolean indexing flattens arrays by default.

# The values corresponding to True are [6, 8, 11, 13].