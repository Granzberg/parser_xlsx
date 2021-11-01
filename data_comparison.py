import pandas as pd
import sort_data_analisys as da

data = {}
data_choice = ['names', 'emails']
fn = './processed_data/teachers_moodle.xlsx'


def some_data(some_new_data):
    # Извлечение данных(имен и почт) из списка пользователй moodle(сортированый)
    classes_data = []
    names = handler_of_data(some_new_data, 0)
    emails = handler_of_data(some_new_data, 1)
    # classes_data.append(names)
    # classes_data.append(emails)
    return names


def handler_of_data(input_data, number):
    # Процесс сортировки данных и формирование его в списки
    some_data = []
    for i in input_data[data_choice[number]]:
        some_data.append(i)
    return some_data


def data_comparison(new_list, list_basic_data):
    # процесс сравнивания двух списков...
    print(len(new_list), new_list)
    print(len(list_basic_data), list_basic_data)
    result = list(set(list_basic_data) - set(new_list))
    print(len(result),result)
    # Возврат отсортированиго списка с вычетом почт из moodle...
    return result



xlsx = pd.read_excel(fn, 0, usecols=data_choice, index_col=None)
data.update(xlsx)

list_of_new_data = some_data(data)
basic_data = da.comparison_data

data_comparison(list_of_new_data, basic_data)
