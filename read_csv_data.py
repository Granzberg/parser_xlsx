import pandas as pd

# !!Требуется выполнить первым после копирования csv файла!!
# Чтение полного списка пользователей(csv файла)
data = pd.read_csv('./processed_data/data_users.csv', delimiter=',')

df1 = pd.DataFrame(data)

# Пересоздание прочитаного csv файла в xlsx
with pd.ExcelWriter('./processed_data/read_data.xlsx') as writer:
    df1.to_excel(writer, sheet_name="Sheet1")
