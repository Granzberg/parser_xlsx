import pandas as pd

data = pd.read_csv('data_users.csv', delimiter=',')

df1 = pd.DataFrame(data)

with pd.ExcelWriter('./read_data.xlsx') as writer:
    df1.to_excel(writer, sheet_name="Sheet1")
