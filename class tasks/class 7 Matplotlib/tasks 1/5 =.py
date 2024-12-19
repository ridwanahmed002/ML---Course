# ContourPlot.py

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-5, 5, 0.25)
y = np.arange(-5, 5, 0.25)
x, y = np.meshgrid(x, y)
r = np.sqrt(x**2 + y**2)
z = np.sin(r)

plt.contourf(x, y, z)
plt.show()