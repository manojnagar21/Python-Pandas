import pandas as pd

df1 = pd.DataFrame({"A": [1, 2], "B": [3, 4], "C": [1, 2]})
df2 = pd.DataFrame({"A": [5, 6], "B": [7, 8]})
print(df1)
print(df2)
result = pd.concat([df1, df2], axis=0)
print(result)
result = pd.concat([df1, df2], axis=0, ignore_index=True)
print(result)
result = pd.concat([df1, df2], axis=1)
print(result)


df4 = pd.DataFrame({"A": [10, 20], "D": [30, 40]})
print(df4)
result = pd.concat([df1, df4], ignore_index=True)
print(result)



result = pd.concat([df1, df2], keys=["first", "second"])

print(result)

# result = df1.append(df2)

# print(result)

new_row = {"A": 100, "B": 200}
df1 = pd.concat([df1, pd.DataFrame([new_row])], ignore_index=True)
print(df1)


s1 = pd.Series([1, 2])
s2 = pd.Series([3, 4])
result = pd.concat([s1, s2])

print(result)