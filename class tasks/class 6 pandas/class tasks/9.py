# Example 21: Pandas - Using applymap for Element-wise 

import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})

df.applymap(lambda x: x * 2) 

print(df)