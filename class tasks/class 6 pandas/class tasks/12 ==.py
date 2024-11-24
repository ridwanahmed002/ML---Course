# Example 48: Pandas - Detecting and Replacing Outliers

import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})

outliers = df[(df['A'] < 3) | (df['A'] > 7)]

df.loc[outliers.index, 'A'] = df['A'].mean()

print(df)