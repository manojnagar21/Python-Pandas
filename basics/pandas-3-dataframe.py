"""
What is a DataFrame?
A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.
"""

import pandas as pd;
data = {
    "id": [1, 2, 3],
    "name": ["Rohan", "Sohan", "Mohan"],
    "salary": [25000.00, 35000.00, 55000.00]
}
print(data)

df = pd.DataFrame(data)
print(df)
print(df.loc[0])
print(df.loc[0]["name"])
print(df.loc[[0, 1]])
print(df.loc[[0, 1]]["name"])


index = ["e1", "e2", "e3"]
df = pd.DataFrame(data, index = index)
print(df)
print(df.loc["e1"])
print(df.loc["e1"]["name"])