# Example 40: Pandas - Using drop_duplicates() for Unique Rows

import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3, 1, 2], 'B': [4, 5, 6, 4, 5], 'C': [7, 8, 9, 7, 8]})

#    A  B  C
# 0  1  4  7
# 1  2  5  8
# 2  3  6  9
# 3  1  4  7  # Duplicate of row 0
# 4  2  5  8  # Duplicate of row 1

unique_df = df.drop_duplicates()

print(unique_df)