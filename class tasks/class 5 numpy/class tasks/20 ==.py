# Example 29: NumPy - Using np.choose for Multiple Conditions

import numpy as np

array = np.array([0, 1, 2, 0, 1])  # Only values 0, 1, and 2 as indices
choices = [array, array * 2, array * 3]

result = np.choose(array, choices)
print(result) # [0, 2, 6, 0, 2]

# np.choose(array, choices) will create a new array, result, by choosing elements based on the indices in array.
# Each element in array determines which array in choices to select from:
# array[0] = 0: Selects from choices[0] at position 0, which is 0.
# array[1] = 1: Selects from choices[1] at position 1, which is 2.
# array[2] = 2: Selects from choices[2] at position 2, which is 6.
# array[3] = 0: Selects from choices[0] at position 3, which is 0.
# array[4] = 1: Selects from choices[1] at position 4, which is 2.