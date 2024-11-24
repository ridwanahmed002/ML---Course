# Example 24: Pandas - Assign Method for Adding Columns

import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Score': [85, 90, 95]}

df = pd.DataFrame(data)

df['Rank'] = [1, 2, 3]

print(df)