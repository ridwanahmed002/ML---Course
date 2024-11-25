# Example 46: Pandas - Working with Time Zones

import pandas as pd

df = pd.DataFrame({'Date': ['2023-01-01', '2023-01-02', '2023-01-03']})

df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')

df['Date'] = df['Date'].dt.tz_localize('UTC')

print(df)