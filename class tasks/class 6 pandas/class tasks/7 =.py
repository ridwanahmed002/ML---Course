# Example 3: Pandas - Using Apply with Lambda Functions

import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
# This creates a DataFrame with three columns A, B, and C:
#    A  B  C
# 0  1  4  7
# 1  2  5  8
# 2  3  6  9
df = df.apply(lambda x: x * 2)

print(df)