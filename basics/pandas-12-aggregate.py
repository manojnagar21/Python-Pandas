import pandas as pd

df = pd.DataFrame({
    'department': ['HR', 'IT', 'HR', 'IT', 'Sales'],
    'salary': [40000, 50000, 45000, 55000, 30000],
    'age': [25, 30, 28, 35, 22]
})
print(df)

print(df.groupby('department')['salary'].mean())
result = df.groupby('department')['salary'].agg(['sum', 'mean', 'max', 'min'])
print(result)


df2 = pd.DataFrame({
    'department': ['HR', 'HR', 'IT', 'IT', 'IT'],
    'gender': ['M', 'F', 'F', 'M', 'F'],
    'salary': [40000, 45000, 50000, 55000, 52000]
})
print(df2)
print(df2.groupby(['department', 'gender'])['salary'].mean())
print(df.groupby('department')['salary'].describe())

filtered = df.groupby('department').filter(
    lambda x: x['salary'].mean() > 50000
)
print(filtered)


def salary_range(x):
    return x.max() - x.min()

result = df.groupby('department')['salary'].agg(salary_range)
print(result)

result = df.groupby('department').agg({
    'salary': ['sum', 'mean'],
    'age': ['min', 'max']
})
print(result)



sales = pd.DataFrame({
    'product': ['A', 'A', 'B', 'B', 'C'],
    'qty': [10, 5, 8, 3, 7],
    'price': [100, 100, 200, 200, 150]
})
print(sales)
sales['revenue'] = sales['qty'] * sales['price']
print(sales)
result = sales.groupby('product')['revenue'].sum()
print(result)