"""
What is a Series?
A Pandas Series is like a column in a table.

It is a one-dimensional array holding data of any type.
"""

import pandas as pd
data = [5, 5.3, "a", True, [1, 2, 3, 4, 5], 1 + 2j, None]
print(data)
series = pd.Series(data)
print(series)


index = ["int", "float", "string", "boolean", "list", "complex", "none"]
series = pd.Series(data, index = index)
print(series)




series = pd.Series([1, 2, 3])
print(series)

series = pd.Series([1, 2, 3], dtype="f4")
print(series)