# Example 25: NumPy - Masked Indexing with np.ma.masked_where

import numpy as np

array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
mask =  array % 2 == 0
masked_array = np.ma.masked_where(mask, array)
print(masked_array) #[1 -- 3 -- 5 -- 7 -- 9 --]