# Example 29: Pandas - Sorting by Multiple Columns

import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 7, 6], 'C': [7, 8, 9]})

sorted_df = df.sort_values(by=['A', 'C'], ascending=[True, False])

print(sorted_df)