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
    return emails


def handler_of_data(input_data, number):
    some_data = []
    for i in input_data[data_choice[number]]:
        some_data.append(i)
    return some_data


def data_comparison(new_list, list_basic_data):
    list_2 = {str(new_list)}
    list_1 = {str(list_basic_data)}
    # data_choice = set(list_1 | list_2)
    # table_format = '{:<10} {:<10}'
    # print(table_format.format('list_1', 'list_2'))
    # print('-' * 20)
    # for elem in sorted(data_choice):
    #     if elem in list_1:
    #         if elem in list_2:
    #             print(table_format.format(elem, elem))
    #
    #         else:
    #             print(table_format.format(elem, 'Missing'))
    #     else:
    #         print(table_format.format('Missing', elem))
    print(list_1)

xlsx = pd.read_excel(fn, 0, usecols=data_choice, index_col=None)
data.update(xlsx)

list_of_new_data = some_data(data)
basic_data = da.sorted_data
data_comparison(list_of_new_data, basic_data)