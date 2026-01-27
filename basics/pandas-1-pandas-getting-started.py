import pandas as pd
print(pd.__version__)
data = {
    "id": [123, 456, 789],
    "name": ["Roha", "Sohan", "Mohan"],
    "salary": [25000.00, 35000.00, 55000.00]
}
print(data)
dataframe = pd.DataFrame(data)
print(dataframe)