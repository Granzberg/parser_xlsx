import pandas as pd

data = {}
data_choice = ['First Name [Required]',	'Last Name [Required]',	'Email Address [Required]']
fn = './read_data.xlsx'


# Нужно сделать итерацию и сравнение каждой строки со списком .... и вывода похожих строк в отдельный файл..
xlsx = pd.read_excel(fn, 0, usecols=data_choice, index_col=None)
data.update(xlsx)

print(data)