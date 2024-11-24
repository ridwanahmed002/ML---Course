# Example 10: Pandas - Creating Custom Categorical Data

import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Score': [85, 90, 95]}

df = pd.DataFrame(data)

df['Rank'] = pd.Categorical.from_codes([0, 1, 2], categories=['Low', 'Medium', 'High'])

print(df)