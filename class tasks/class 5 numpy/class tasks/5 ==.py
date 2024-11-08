#NumPy - Advanced Slicing with Step in 2D Array

import numpy as np

array = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(array[0, 1:4:2]) # here 1:4:2 means 1,3

slicing = array[::2, ::3] # here ::2 means 0,2 ; ::3 means 0,3

#::2 on the row axis means: Start from the beginning (0), go until the end, and take every second row. Since there are only two rows, this selects only the first row (index 0).

#::3 on the column axis means: Start from the beginning (0), go until the end, and take every third column.This selects columns 0 and 3.

print(slicing)

slicing2 = array[::3, ::2]# here ::3 means 0,3 ; ::2 means 0,2

#::3 on the row axis means: Start from the beginning (0), go until the end, and take every third row. Again, with only two rows, this selects only the first row (index 0).

# ::2 on the column axis means: Start from the beginning (0), go until the end, and take every second column.This selects columns 0, 2, and 4.

print(slicing2)