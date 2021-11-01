import pandas as pd

data = {}
data_choice = ['First Name [Required]',	'Last Name [Required]',	'Email Address [Required]']
fn = './processed_data/read_data.xlsx'


def sort_data(data_list):
    # Создание трех списков с разными данными
    name = transformation(data_list, 0) # Имена
    surname = transformation(data_list, 1) # Фамили
    email = transformation(data_list, 2) # Почты

    list_of_full_name = []
    for i in range(len(name)):  # Обьединение в один список Имен и Фимилй
        list_of_full_name.append(name[i] + ' ' + surname[i])
    return list_of_full_name


def comparison(data_list):
    # Создание списка дубликатов имен и фамилий...?
    sorted_my_list = create_words(data_list, 1)
   # print(sorted_my_list)
    a_data = []
    for i in set(sorted_my_list):
        if sorted_my_list.count(i) > 1:
            a_data.append(i)

    return a_data


def transformation(all_data, number):
    # Процес создания списка с опредиленными настройками( Имена, фимилии, почты)
    data_clean = []
    for i in all_data[data_choice[number]]:
        data_clean.append(i)

    return data_clean


def create_words(names, k):
    # создание списка
    j = []
    for i in names[0]:
        j.append(i)
    j = [item.split() for item in j]
    l = len(j)
    names_list = []

    for n in range(0, l):
        # k примает переданое занчение из функции и тем самым происходит раздиление по назначению..
        if k == 1:
            for i in j[n][1:2]:
                names_list.append(i)
        else:
            for i in j[n][:1]:
                names_list.append(i)
    return names_list


xlsx = pd.read_excel(fn, 0, usecols=data_choice, index_col=None)
data.update(xlsx)

sorted_data = sort_data(data)
comparison_data = comparison([sort_data(data)])

print(sorted_data)

df1 = pd.DataFrame(sorted_data)


# Запись сортированых данных в xlsx
with pd.ExcelWriter('./processed_data/duplicate_names.xlsx') as writer:
    df1.to_excel(writer, sheet_name="Sheet1")

