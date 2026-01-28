"""
Read CSV Files
A simple way to store big data sets is to use CSV files (comma separated files).

CSV files contains plain text and is a well know format that can be read by everyone including Pandas.
"""

import pandas as pd
# df = pd.read_csv("d:\folder\data.csv")
df = pd.read_csv("data.csv")
print(df.to_string())
print(df)
print(pd.options.display.max_rows)
pd.options.display.max_rows = 300
print(pd.options.display.max_rows)
print(df)
print(df.head(10))
print(df.tail(10))
print(df.info()) 