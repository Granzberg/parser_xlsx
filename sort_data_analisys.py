import pandas as pd

data = {}
data_choice = ['First Name [Required]',	'Last Name [Required]',	'Email Address [Required]']
fn = './read_data.xlsx'


def sort_data(data_list):
    name = transformation(data_list, 0)
    surname = transformation(data_list, 1)
    email = transformation(data_list, 2)

    list_of_full_name = []
    for i in range(len(name)):
        list_of_full_name.append(name[i] + ' ' + surname[i])

    return list_of_full_name


def comparison(data_list):
    my_list = data_list
    a_data = []
    for i in set(my_list):
        if my_list.count(i) > 1:
            a_data.append([i, my_list.index(i)])
    return a_data


def transformation(all_data, number):
    data_clean = []
    for i in all_data[data_choice[number]]:
        data_clean.append(i)
    return data_clean


xlsx = pd.read_excel(fn, 0, usecols=data_choice, index_col=None)
data.update(xlsx)

sorted_data = comparison(sort_data(data))

df1 = pd.DataFrame(sorted_data)

with pd.ExcelWriter('./duplicate_names.xlsx') as writer:
    df1.to_excel(writer, sheet_name="Sheet1")

