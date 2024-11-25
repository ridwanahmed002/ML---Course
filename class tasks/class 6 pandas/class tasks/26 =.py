# Example 56: Pandas - Stacking and Unstacking DataFrames

import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})

stacked_df = df.stack()
unstacked_df = stacked_df.unstack()

print('Stacked DataFrame:\n', stacked_df)
print('Unstacked DataFrame:\n', unstacked_df)