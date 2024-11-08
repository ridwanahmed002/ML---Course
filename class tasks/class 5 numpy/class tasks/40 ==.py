# Example 18: NumPy - Meshgrid Creation

import numpy as np

array_1 = np.array([1, 2, 3])
array_2 = np.array([4, 5, 6])

meshgrid = np.meshgrid(array_1, array_2)
print(meshgrid)

# The np.meshgrid function takes two or more 1D arrays and returns two 2D arrays (or more, if there are more inputs). In this case, you are passing two 1D arrays array_1 and array_2.

# The function works by creating a grid where:

# The first returned array (meshgrid[0]) contains copies of array_1 repeated along rows.
# The second returned array (meshgrid[1]) contains copies of array_2 repeated along columns.
# The result will be two 2D arrays where the first one has the shape of (len(array_2), len(array_1)) and the second one has the same shape, but with values representing the coordinates in the second direction.

# [array([[1, 2, 3],
#         [1, 2, 3],
#         [1, 2, 3]]),
#  array([[4, 4, 4],
#         [5, 5, 5],
#         [6, 6, 6]])]
