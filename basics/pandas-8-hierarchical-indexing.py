import pandas as pd
import numpy as np

data = pd.Series(
    [10, 20, 30, 40],
    index=[["A", "A", "B", "B"], ["x", "y", "x", "y"]]
)

print(data)


arrays = [
    ["India", "India", "USA", "USA"],
    ["Delhi", "Mumbai", "NY", "LA"]
]

df = pd.DataFrame({
    "population": [30, 20, 15, 10],
    "area": [1500, 900, 800, 700]
}, index=arrays)

print(df)

print(df.loc["India"])
print(df.loc["India", "Delhi"])
print(df.loc[("USA", "LA")])

df2 = df.reset_index().set_index(["level_0", "level_1"])
print(df2)
df.sort_index(inplace=True)
print(df)



columns = pd.MultiIndex.from_product(
    [["Math", "Science"], ["Term1", "Term2"]]
)

scores = pd.DataFrame([[50, 60, 70, 80],
                       [60, 50, 70, 80],
                       [70, 50, 60, 80]], columns=columns)
print(scores)

scores.unstack()

print(scores.unstack())

df_group = df.groupby(level=0).sum()
print(df_group)


df_group = df.groupby(level=1).sum()
print(df_group)