# Example 18: Pandas - Detecting Duplicates

import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3, 1, 2], 'B': [4, 5, 6, 4, 5], 'C': [7, 8, 9, 7, 8]})

print(df.duplicated())