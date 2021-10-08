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
    # создание списка имен
    names = {}
    names.update(list_names[words[0]])
    n = []
    for item in names.values():
        n.append(item)
    # print(type(n))
    # print(n)
    return n


def splitting_word_into_letters(data_clean):
    # Раздиление слов на буквы
    separated_words_into_letters = []
    translated_word = []
    for w in data_clean:
        k = list(w)
        separated_words_into_letters.append(k)

    return separated_words_into_letters


def translation_of_word(list_of_words, dictionary):
    w = 0
    words = []
    for word in list_of_words[w]:
        for letter in word:
            words.append(letter.lower())
    print(words)
    for k,v in dictionary.items():
        n = {k: dictionary[k] for k in dictionary.keys() & set(list_of_words)}
        print(n)





xlsx = pd.read_excel(fn, 0, usecols=words, index_col=None)
data.update(xlsx)

w = splitting_word_into_letters(create_list_of_word(xlsx))
translation_of_word(w, letters)