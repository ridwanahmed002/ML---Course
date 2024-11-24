# Example 35: Pandas - Using at and iat for Fast Scalar Access

import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})

print(df.at[0, 'A'])
print(df.at[1, 'B'])
print(df.iat[0, 0])
print(df.iat[1, 1])
