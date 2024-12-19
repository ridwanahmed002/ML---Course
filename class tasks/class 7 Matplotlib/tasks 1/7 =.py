# BoxenPlot.py

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = np.random.normal(size=1000)
sns.boxenplot(x=data)
plt.title('Boxen Plot Example')
plt.xlabel('Values')
plt.show()