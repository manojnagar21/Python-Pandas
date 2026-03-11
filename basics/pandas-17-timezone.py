import pandas as pd

dt = pd.to_datetime("2025-01-10 10:00:00")
aware = dt.tz_localize("UTC")
print(aware)
ist = aware.tz_convert("Asia/Kolkata")
print(ist)


rng = pd.date_range("2025-01-01", periods=4, freq="D")
series = pd.Series([10, 20, 30, 40], index=rng)
print(series)
# Add timezone
series = series.tz_localize("UTC")
# Convert to IST
series_ist = series.tz_convert("Asia/Kolkata")
print(series_ist)


df = pd.DataFrame({
    "time": ["2025-01-10 10:00:00+00:00", "2025-01-10 18:30:00+05:30"]
})
print(df)
df["time"] = pd.to_datetime(df["time"], utc=True)
print(df)


naive = aware.tz_convert("UTC").tz_localize(None)
print(naive)


# df = pd.DataFrame({
#     "user": ["A", "B", "C"],
#     "login_time": [
#         "2025-01-10 18:00:00 US/Eastern",
#         "2025-01-10 15:00:00 Europe/London",
#         "2025-01-11 10:00:00 Asia/Tokyo"
#     ]
# })
# print(df)
# df["login_time"] = pd.to_datetime(df["login_time"], utc=True, format="mixed")
# # Normalize everything to IST
# df["ist_time"] = df["login_time"].dt.tz_convert("Asia/Kolkata")
# print(df)



# df["tz"] = df["login_time"].dt.tz
# print(df["tz"])