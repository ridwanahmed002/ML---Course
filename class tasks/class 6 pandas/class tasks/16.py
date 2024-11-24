# Example 22: Pandas - Creating Dummy Variables

import pandas as pd

df = pd.DataFrame({'Color': ['Red', 'Green', 'Blue', 'Red', 'Green']})

dummy_df = pd.get_dummies(df['Color'])

print(dummy_df)