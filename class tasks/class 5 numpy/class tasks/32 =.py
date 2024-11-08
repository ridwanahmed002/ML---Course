# Example 7: NumPy - Reshaping Arrays

import numpy as np

array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(array.reshape(2, 5)) # [[ 1  2  3  4  5] [ 6  7  8  9 10]]    
print(array.reshape(5, 2)) # [[ 1  2] [ 3  4] [ 5  6] [ 7  8] [ 9 10]]