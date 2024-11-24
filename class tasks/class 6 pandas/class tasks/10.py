# Example 34: Pandas - Adding a Prefix or Suffix to Column Names

import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})

df_prefix = df.add_prefix('col_')
df_suffix = df.add_suffix('_col')

print(df_prefix)
print(df_suffix)