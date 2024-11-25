# Example 12: Pandas - Shift and Lagging Data

import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3, 4, 5]})

shifted_df = df.shift(periods=1)

print('Shifted DataFrame:\n', shifted_df)