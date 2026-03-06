import pandas as pd

s = pd.Series(["Hello", "WORLD", "Python"])
print(s)
print(s.str.lower())
print(s.str.upper())

s = pd.Series(["  apple  ", "\tbanana\n"])
print(s)
print(s.str.strip())     # remove spaces & tabs both sides
print(s.str.lstrip())    # left
print(s.str.rstrip())    # right

s = pd.Series(["cat", "elephant", "", None])
print(s)
print(s.str.len())

s = pd.Series(["a-b-c", "1-2-3"])
print(s)
print(s.str.split("-"))
print(s.str.split("-")[1])     # second part
print(s.str.split("-").str[1])     # second part

s = pd.Series(["hello123", "abc456"])
print(s)
print(s.str.replace(r'\d+', '', regex=True))

s = pd.Series(["python code", "java app", "python script"])
print(s)
print(s.str.contains("python")) # case sensitive
print(s.str.startswith("py"))
print(s.str.endswith("app"))


s = pd.Series(["A10", "B20", "C300 500"])
print(s)
print(s.str.extract(r'(\d+)'))     # returns DataFrame

s = pd.Series(["Name: John, Age: 30"])
print(s)
print(s.str.extract(r'Name: (\w+), Age: (\d+)'))


s = pd.Series(["Name: John, Age: a30"])
print(s)
print(s.str.extract(r'Name: (\w+), Age: (\d+)'))

s = pd.Series(["apple banana", "banana mango"])
print(s)
print(s.str.replace("banana", "grapes"))


s = pd.Series(["A", "B", "C"])
print(s)
print(s.str.cat(sep='-'))    # A-B-C

df = pd.DataFrame({
    'first': ['John', 'Alice'],
    'last': ['Doe', 'Smith']
})
print(df)
df['full'] = df['first'].str.cat(df['last'], sep=' ')
print(df)


users = pd.Series([
    "  MRITUNJAY  NAGAR ",
    "john_doe123",
    "ALICE.SMITH"
])
print(users)
clean = (users
    .str.strip()
    .str.lower()
    .str.replace(r'[\W_]+', ' ', regex=True)
    .str.replace(r'[\d+]+', ' ', regex=True)
    .str.title()
)

print(clean)