import pandas as pd

df1 = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'salary': ["A", "B", "C", "D"],
    'name': ['Amit', 'Maya', 'John', 'Sara']
})
df2 = pd.DataFrame({
    'id': [3, 4, 5, 6],
    'salary': [30000, 40000, 35000, 28000],
    'name': ["a", "b", "c", "d"]
})
print(df1)
print(df2)


result = pd.merge(df1, df2, on="id", how="inner", suffixes=("_left", "_right"))
print(result)
result = pd.merge(df1, df2, on='id', how='left', suffixes=("_left", "_right"))
print(result)
result = pd.merge(df1, df2, on='id', how='right', suffixes=("_left", "_right"))
print(result)
result = pd.merge(df1, df2, on='id', how='outer', suffixes=("_left", "_right"))
print(result)

df1 = df1.set_index('id')
df2 = df2.set_index('id')

result = df1.join(df2, how='inner', lsuffix="_left", rsuffix="_right")
print(result)

result = df1.join(df2, how='left', lsuffix="_left", rsuffix="_right")
print(result)



result = df1.join(df2, how='right', lsuffix="_left", rsuffix="_right")
print(result)

result = df1.join(df2, how='outer', lsuffix="_left", rsuffix="_right")
print(result)