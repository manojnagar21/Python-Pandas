import pandas as pd

df = pd.DataFrame({
    'Date': ['2025-01', '2025-01', '2025-02'],
    'Product': ['A', 'B', 'A'],
    'Sales': [100, 150, 120]
})
print(df)
grouped = df.groupby('Product')['Sales'].sum()
print(grouped)

pt = df.pivot_table(
    index="Product",
    # columns="Date",
    values="Sales",
    aggfunc="sum",
    fill_value=0
)
print(pt)


df = pd.DataFrame({
    'Gender': ['M','F','M','F','M'],
    'Course': ['Python','Python','Java','Java','Python']
})
print(df)
ct = pd.crosstab(df['Gender'], df['Course'])
print(ct)

df2 = pd.DataFrame({
    'Team': ['A','A','B','B', 'A', 'B'],
    'Player': ['X','Y','X','Y', 'X', 'Y'],
    'Score': [10, 20, 30, 40, 20, 20]
})
print(df2)
ct2 = pd.crosstab(df2['Team'], df2['Player'], values=df2['Score'], aggfunc='sum')
print(ct2)