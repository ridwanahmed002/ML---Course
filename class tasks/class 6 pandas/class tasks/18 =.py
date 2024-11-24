# Example 38: Pandas - Creating Custom Aggregations with Groupby

import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})

grouped_df = df.groupby('A').agg({'B': 'sum', 'C': 'mean'})

# groupby('A'): Groups the DataFrame by the values in column A. Since each value in A is unique (1, 2, and 3), each row becomes its own group.
# .agg({'B': 'sum', 'C': 'mean'}):
# Specifies custom aggregation functions for the grouped data.
# For column B: Apply the sum function (adds all values in the group).
# For column C: Apply the mean function (calculates the average of values in the group).

print(grouped_df)