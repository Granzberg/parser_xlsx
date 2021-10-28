import pandas as pd
import sort_data_analisys as da

data = {}
data_choice = ['names', 'emails']
fn = './teachers_moodle.xlsx'


def some_data(some_new_data):
    classes_data = []
    names = handler_of_data(some_new_data, 0)
    emails = handler_of_data(some_new_data, 1)
    classes_data.append(names)
    classes_data.append(emails)
    return classes_data


def handler_of_data(input_data, number):
    some_data = []
    for i in input_data[data_choice[number]]:
        some_data.append(i)
    return some_data


def data_comparison(new_list, list_basic_data):
    data_choice = []
    for i in range(len(list_basic_data)):
        for y in set(list_basic_data[i]):
            if new_list.count(i) == list_basic_data[i]:
                print(list_basic_data[y])




xlsx = pd.read_excel(fn, 0, usecols=data_choice, index_col=None)
data.update(xlsx)

list_of_new_data = some_data(data)
basic_data = da.sorted_data
data_comparison(list_of_new_data, basic_data)