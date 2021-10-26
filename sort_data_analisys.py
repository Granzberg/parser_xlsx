import pandas as pd

data = {}
data_choice = ['First Name [Required]',	'Last Name [Required]',	'Email Address [Required]']
fn = './read_data.xlsx'


def sort_data(data_list):
    data = []
    for i in data_list[data_choice[0]]:
        print(i)



# Нужно сделать итерацию и сравнение каждой строки со списком .... и вывода похожих строк в отдельный файл..
xlsx = pd.read_excel(fn, 0, usecols=data_choice, index_col=None)
data.update(xlsx)

sort_data(data)
