# Example 19: NumPy - Clipping Array Values

import numpy as np

array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

clipped_array = np.clip(array, 5, 9)

print(clipped_array) # [5, 5, 5, 5, 5, 6, 7, 8, 9, 9]

# The np.clip function constrains each element in array within the specified minimum (5) and maximum (9) values:

# Any element less than 5 will be set to 5.
# Any element greater than 9 will be set to 9.
# Elements between 7 and 8 (inclusive) will remain unchanged.