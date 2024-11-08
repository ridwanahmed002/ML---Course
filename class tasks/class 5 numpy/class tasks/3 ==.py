import numpy as np

array_1 = np.array([[1, 2], [4, 5]])
array_2 = np.array([[7, 8], [10, 11]])

#creating meshgrid
meshgrid = np.meshgrid(array_1, array_2)
print(meshgrid) #