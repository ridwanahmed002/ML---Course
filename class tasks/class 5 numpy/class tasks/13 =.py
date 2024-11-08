# Example 20: NumPy - Cumulative Sum and Product

import numpy as np

array = np.array([1, 2, 3, 4, 5])

cumulative_sum = np.cumsum(array)
cumulative_product = np.cumprod(array)

print(cumulative_sum) # [1, 3, 6, 10, 15]
print(cumulative_product) # [1, 2, 6, 24, 120]