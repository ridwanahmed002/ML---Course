# Example 41: Pandas - Combining DataFrames with Multi-level Indexes

import pandas as pd

df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
df2 = pd.DataFrame({'A': [10, 20, 30], 'B': [40, 50, 60], 'C': [70, 80, 90]})

combined_df = pd.concat([df1, df2], keys=['df1', 'df2'])

print(combined_df)