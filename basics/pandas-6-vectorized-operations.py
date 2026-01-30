import pandas as pd

df = pd.DataFrame({
    "price": [100, 200, 300],
    "quantity": [3, 2, 5]
})

print(df)
df["total"] = df["price"] * df["quantity"]   # vectorized
print(df)

print(df["price"].sum())      # total
print(df["price"].mean())     # average
print(df["price"].max())      # highest
print(df["price"].min())      # lowest
print(df.describe())          # full statistics summary

df["discount_price"] = df["price"].apply(lambda x: x * 0.9)
print(df)


print(df.applymap(lambda x: x * 2)) # deprecated
print(df.map(lambda x: x * 2))


df["row_sum"] = df.apply(lambda row: row["price"] + row["quantity"], axis=1)
print(df)


df2 = pd.DataFrame({"name": ["amit", "RITA", "john"]})
print(df2)
print(df2["name"].str.upper())
print(df2["name"].str.contains("it"))

import numpy as np
df3 = pd.DataFrame({"a":[1,2,np.nan], "b":[4,np.nan,6]})
print(df3)

print(df3.sum())          # NaN ignored by default
print(df3.mean(skipna=False))   # does not ignore