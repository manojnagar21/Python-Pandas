import pandas as pd
from functools import reduce
sales = pd.DataFrame({
    'product_id': [101, 102, 103],
    'qty': [3, 4, 2]
})
products = pd.DataFrame({
    'pid': [101, 102, 104],
    'price': [100, 200, 120]
})
print(sales)
print(products)
result = pd.merge(sales, products, left_on='product_id', right_on='pid', how='left')
print(result)

students = pd.DataFrame({
    'roll': [1, 2, 3],
    'name': ['Amit', 'Rahul', 'Sara']
})
marks = pd.DataFrame({
    'id': [2, 3, 4],
    'math': [88, 77, 91]
})
result = pd.merge(students, marks, left_on="roll", right_on="id", how="inner")
print(result)

emp = pd.DataFrame({
    'eid': [1, 2, 3],
    'ename': ['Amit', 'Maya', 'John']
})
dept = pd.DataFrame({
    'eid': [2, 3, 4],
    'dept': ['HR', 'IT', 'Finance']
})
result = pd.merge(emp, dept, on="eid", how="outer")
print(result)

att = pd.DataFrame({
    'id': [1, 1, 2],
    'date': ['2025-01-01', '2025-01-02', '2025-01-01'],
    'status': ['P', 'A', 'P']
})
ded = pd.DataFrame({
    'id': [1, 1, 2],
    'date': ['2025-01-02', '2025-01-01', '2025-01-01'],
    'deduct': [500, 0, 200]
})
result = pd.merge(att, ded, on=["id", "date"], how="inner")
print(result)

df1 = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['Amit', 'Maya', 'John', 'Sara']
})
df2 = pd.DataFrame({
    'id': [3, 4, 5, 6],
    'salary': [30000, 40000, 35000, 28000]
})
df1 = df1.set_index('id')
df2 = df2.set_index('id')
result = df1.join(df2, how='left')
print(result)

emp = pd.DataFrame({
    'eid': [1, 2, 3],
    'name': ['Amit', 'Maya', 'John']
})
dept = pd.DataFrame({
    'eid': [1, 2, 3],
    'dept': ['HR', 'IT', 'Finance']
})
sal = pd.DataFrame({
    'eid': [1, 2, 3],
    'salary': [50000, 60000, 55000]
})
emp_dept = pd.merge(emp, dept, on="eid", how="left")
print(emp_dept)
emp_dept_sal = pd.merge(emp_dept, sal, on="eid", how="left")
print(emp_dept_sal)
final = emp.merge(dept, on='eid').merge(sal, on='eid')
print(final)
final = pd.merge(emp, dept, on='eid', how="left").merge(sal, on='eid')
print(final)


df = [emp, dept, sal]
result = reduce(lambda left, right: pd.merge(left, right, on="eid", how="left"), df)
print(result)