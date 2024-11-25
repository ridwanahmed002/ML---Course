# Example 30: Pandas - Using style for DataFrame Styling

import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})

df.style.background_gradient(cmap='coolwarm')

print(df)