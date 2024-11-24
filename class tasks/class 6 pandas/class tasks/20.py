# Example 13: Pandas - Cumulative Sum and Product

import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3, 4, 5]})

cumulative_sum = df.cumsum()
cumulative_product = df.cumprod()

print(cumulative_sum)
print(cumulative_product)