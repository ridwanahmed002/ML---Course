# Example 47: Pandas - Using pd.cut for Binning Data

import pandas as pd

ages = [20, 22, 25, 27, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]

df = pd.DataFrame({'Age': ages})

df['Age_Bin'] = pd.cut(df['Age'], bins=[0, 20, 30, 40, 50, 60, 70, 80, 90, 100], labels=['<20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80', '80-90', '90-100'])

print(df)