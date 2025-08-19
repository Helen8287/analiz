import pandas as pd

df = pd.read_csv('zarplata.csv')
print(df.info())

print(df.tail())

print(df.describe())

group = df.groupby('City')['Salary'].mean()
print(group)

