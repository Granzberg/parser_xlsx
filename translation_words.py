import pandas as pd
fn = './test.xlsx'
words = ['Name', 'Surname']
data = {}

letters = {'а': 'a', 'б': 'd', 'в': 'v', 'г': 'h', 'ґ': 'g', 'д': 'd', 'е': 'e', 'є': 'ye', 'ж': 'zh', 'з': 'z',
           'и': 'y','і': 'i', 'ї': 'yi', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'р': 'r',
           'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'kh', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ю': 'yu', 'я': 'ya',
           'зг': 'zgh'}

alternate_letters = {'є': 'ie', 'ї': 'i', 'й': 'i', 'ю': 'iu', 'я': 'ia'}


def create_list_of_word(list_names):
    names = {}
    data_clean = []
    names.update(list_names[words[0]])
    n = []
    for item in names.values():
        n.append(item)

    return n


def translation_of_word(data_clean):
    for i in data_clean:
        length = len(i)
        for l in range(length):
            pass


xlsx = pd.read_excel(fn, 0, usecols=words, index_col=None)
data.update(xlsx)

w = create_list_of_word(xlsx)

translation_of_word(w)
