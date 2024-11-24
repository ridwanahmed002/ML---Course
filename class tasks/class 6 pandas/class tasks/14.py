# Example 49: Pandas - Using DataFrame.eval for Efficient Calculations

import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})

result = df.eval('A + B + C')

print(result)