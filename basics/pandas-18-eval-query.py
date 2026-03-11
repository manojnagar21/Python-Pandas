import pandas as pd

df = pd.DataFrame({
    'price': [100, 200, 150],
    'qty': [2, 3, 4]
})
print(df)
# Using eval
# df['total'] = df["price"] * df["qty"]
df['total'] = df.eval("price * qty")
print(df)


df.eval("""
    discount = price * 0.10
    final = price - discount
""", inplace=True)
print(df)

df['is_high_value'] = df.eval("final > 150")
print(df)

df.query("price > 100 & qty < 4")
print(df)
filtered = df.query("price > 120")
print(filtered)
min_price = 120
df.query("price > @min_price")


df2 = pd.DataFrame({
    'name': ["apple", "banana", "grapes", "apricot"],
    'price': [50, 40, 60, 70]
})
print(df2)
result = df2.query("name.str.startswith('a')")
print(result)

sales = pd.DataFrame({
    'product': ['A','B','C','D'],
    'price': [500, 800, 300, 900],
    'qty': [5, 3, 8, 2],
    'category': ['mobile','mobile','laptop','mobile']
})
print(sales)
# Create revenue
sales.eval("revenue = price * qty", inplace=True)
print(sales)
# Filter high revenue mobiles
result = sales.query("category == 'mobile' & revenue > 2000")
print(result)