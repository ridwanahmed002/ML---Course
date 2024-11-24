# Example 9: Pandas - Conditional Filtering with Multiple Conditions

import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})

filtered_df = df[(df['A'] > 2) & (df['B'] < 6)]

print(filtered_df)