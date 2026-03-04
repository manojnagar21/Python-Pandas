import pandas as pd

df = pd.DataFrame({
    'department': ['HR', 'HR', 'IT', 'IT', 'Sales', 'Sales'],
    'gender': ['M', 'F', 'F', 'M', 'F', 'M'],
    'salary': [40000, 45000, 50000, 55000, 30000, 32000]
})
print(df)

table = df.pivot_table(
    values="salary",
    index="department",
    aggfunc="sum"
)
print(table)


table = df.pivot_table(
    values="salary",
    index="department",
    columns="gender",
    aggfunc="sum"
)
print(table)

table = df.pivot_table(
    values="salary",
    index="department",
    columns="gender",
    aggfunc=["sum", "max", "min", "mean"]
)
print(table)


table = df.pivot_table(
    values=['salary'],
    index='department',
    columns='gender',
    aggfunc={'salary': ["sum", "max", "min", "mean"]}
)

print(table)

table = df.pivot_table(
    values='salary',
    index='department',
    columns='gender',
    aggfunc='mean',
    margins=True,
    margins_name='Total'
)

print(table)

table = df.pivot_table(
    values='salary',
    index='department',
    columns='gender',
    aggfunc='mean',
    fill_value=0
)

print(table)