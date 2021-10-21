import pandas as pd

fn = './test.xlsx'
words = ['Name', 'Surname']
data = {}



xlsx = pd.read_excel(fn, 0, usecols=words, index_col=None)
data.update(xlsx)
