import pandas as pd
data = {
    "name": ["Amit", "Rita", "John"],
    "age": [25, 30, 28],
    "city": ["Delhi", "Mumbai", "Pune"]
}

df = pd.DataFrame(data, index=["a", "b", "c"])
print(df)
print(df.index)
print(df.columns)
print(df.describe() )

print(df["name"])
print(df[["name", "city"]])
print(df[0:2])
print(df.loc["a"])
df = pd.DataFrame(data)
print(df.loc[0:2, ["name", "city"]])
print(df.iloc[1])
print(df.iloc[0:2, 0:2])
print(df["age"] > 27)

print(df[df["age"] > 27])

df2 = df.set_index("name")
print(df2)
print(df2.loc["Amit"])