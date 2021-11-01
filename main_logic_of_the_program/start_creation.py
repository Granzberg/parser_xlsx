import pandas as pd

data = {}
data_choice = ['patronymic', 'spec']
fn = '..//processed_data/test.xlsx'
print('Create xlsx file .....')


def create_list_of_names(list_names):
    # создание списка (0 - имена, 1 - специальности, 2 - корп.почта)
    names = {}
    data_clean = []
    names.update(list_names[data_choice[0]])
    n = []
    for item in names.values():
        n.append(item)
    spec = {}
    spec.update(list_names[data_choice[1]])
    sp = []
    for item in spec.values():
        sp.append(item)

    data_clean.append(n)
    data_clean.append(sp)
    return data_clean


def surname_str(name_s):
    # возврат списка фамилий
    k = 0
    surname = create_words(name_s, k)
    return surname


def names_str(name_s):
    # возврат списка имен
    k = 1
    names = create_words(name_s, k)
    return names


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


def spec_number(spec):
    # создание списка с кодом специальности
    c = []
    for u in spec[1]:
        c.append(u)
    c = [item.split() for item in c]
    l = len(c)
    spec_num = []
    for n in range(0, l):
        for i in c[n][:1]:
            spec_num.append(i)
    return spec_num


# Чтение исходного файла xlsx
xlsx = pd.read_excel(fn, 0, usecols=data_choice, index_col=None)
data.update(xlsx)

list_of_names = create_list_of_names(xlsx)
names_str = names_str(list_of_names)
surname_str = surname_str(list_of_names)
spec_number = spec_number(list_of_names)

df1 = pd.DataFrame({'Name': names_str,
                    'Surname': surname_str,
                    'Specialty number': spec_number})

with pd.ExcelWriter('..//processed_data/translation_names.xlsx') as writer:
    df1.to_excel(writer, sheet_name="Sheet1", index_label="№")
# проблема в xlsx файле ... требуеться переделать формирование файла..
print('Xlsx file done ...')
