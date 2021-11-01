import pandas as pd

data = {}
data_choice = ['First Name [Required]',	'Last Name [Required]',	'Email Address [Required]']
fn = './processed_data/read_data.xlsx'


def sort_data(data_list):
    # Создание трех списков с разными данными
    name = transformation(data_list, 0) # Имена
    surname = transformation(data_list, 1) # Фамили
    email = transformation(data_list, 2) # Почты
    list_of_emails = []
    list_of_full_name = []
    for i in range(len(name)):  # Обьединение в один список Имен и Фимилй
        list_of_full_name.append(name[i] + ' ' + surname[i])
        list_of_emails.append(email[i])  # Переопредиление списка с почтами

    return email


def comparison(data_list):
    # Создание списка для передачи в другой файл...?
    my_list = data_list
    a_data = []
    for i in set(my_list):
        if my_list.count(i) > 1:
            a_data.append([i, my_list.index(i)])
    return a_data


def transformation(all_data, number):
    # Процес создания списка с опредиленными настройками( Имена, фимилии, почты)
    data_clean = []
    for i in all_data[data_choice[number]]:
        data_clean.append(i)

    return data_clean


xlsx = pd.read_excel(fn, 0, usecols=data_choice, index_col=None)
data.update(xlsx)

sorted_data = comparison(sort_data(data))

df1 = pd.DataFrame(sorted_data)
#print(comparison(sort_data(data)))

# Запись сортированых данных в xlsx
with pd.ExcelWriter('./processed_data/duplicate_names.xlsx') as writer:
    df1.to_excel(writer, sheet_name="Sheet1")

