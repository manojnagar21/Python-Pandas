import pandas as pd

dates = pd.to_datetime(["2025-01-01", "2025-02-15", "2025-03-10"])
print(dates)

rng = pd.date_range("2025-01-01", periods=5, freq="D")
print(rng)


ts = pd.Series([10,20,15,30,25], index=rng)
print(ts)


print("---------------------------------------")
print(ts["2025-01-03"])       # exact day
print(ts["2025-01"])          # entire month
print(ts["2025-01-02":"2025-01-04"])  # range






monthly = ts.resample("ME").mean()
print(monthly)


print("---------------------------------------")
print(ts)
upsampled = ts.resample("ME").ffill()
print(upsampled)



print(ts.shift(1))
print(ts.shift(2))
print(ts.shift(-1))

print(ts.shift(-2))

print(ts)
roll = ts.rolling(window=3).mean()
print(roll)


from datetime import timedelta
print(ts.index + timedelta(days=10))
print(ts)

print(ts.index.year)
print(ts.index.month)
print(ts.index.day)
print(ts.index.weekday) # 0 - 6 (Monday - Sunday)

rng = pd.date_range("2025-01-01", periods=10, freq="D")
sales = pd.Series([100,150,120,180,200,170,160,190,210,220], index=rng)
print(sales)
print(sales["2025-01-03":"2025-01-07"])


print("-----------------------------")
weekly = sales.resample("W").sum()
print(weekly)



print(sales)
ma = sales.rolling(3).mean()
print(ma)

print(sales.shift(1))