import pandas as pd
import numpy as np

df = pd.DataFrame({
    "name": ["Amit", None, "John"],
    "age": [25, np.nan, 30],
    "city": ["Delhi", "Mumbai", None]
})
print(df)
print(df.isnull())
print(df.notnull())
print(df.dropna())

print(df.dropna(how="all"))
print(df.dropna(axis=1))
print(df.dropna(thresh=2))
print(df.fillna("Unknown"))

df["age"].fillna(df["age"].mean(), inplace=True)
print(df)

df["city"] = df["city"].fillna("Not Provided")
print(df)


print(df.replace(np.nan, "Missing"))

df2 = pd.DataFrame({
    "name": ["Amit", None, "John"],
    "age": [25, np.nan, 30],
    "city": ["Delhi", "Mumbai", None]
})
print(df2.isnull().any())      # checks column-wise
print(df2.isnull().sum())      # count of missing values per column

print(df2["age"].interpolate())
print(df2)