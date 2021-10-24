import pandas as pd
import translation_words as tw
import create_corporate_email as cce
import start_creation as start

# Создание выборки после парсинга xlsx
names_str = start.names_str
surname_str = start.surname_str
name_TW = tw.name_tw
surname_TW = tw.surname_tw
spec_number = start.spec_number
emails = cce.emails_list

index = []
for i in range(len(names_str)):
    index.append(i+1)

# write to Excel
df1 = pd.DataFrame({'Name': names_str, 'Surname': surname_str, 'Specialty number': spec_number,
                    'Name_TW': name_TW, 'Surname_TW': surname_TW, 'Corp_emails': emails}, index=index)

with pd.ExcelWriter('./translation_names.xlsx') as writer:
    df1.to_excel(writer, sheet_name="Sheet1", index_label="№")
