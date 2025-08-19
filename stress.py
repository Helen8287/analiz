import pandas as pd

df = pd.read_csv('StressLevelDataset (1).csv')
print(df.head())


print(df.info())

print(df.describe())
