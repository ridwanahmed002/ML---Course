# Example 17: Pandas - Using map() for Value Replacement

import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})

df = df.map(lambda x: x * 2)

print(df)