import pandas as pd

fn = './test.xlsx'
words = ['Name', 'Surname']
data = {}

letters = {'а': 'a', 'б': 'd', 'в': 'v', 'г': 'h', 'ґ': 'g', 'д': 'd', 'е': 'e', 'є': 'ye', 'ж': 'zh', 'з': 'z',
           'и': 'y', 'і': 'i', 'ї': 'yi', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'р': 'r',
           'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'kh', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ю': 'yu', 'я': 'ya',
           '1': 'zgh'}

alternate_letters = {'є': 'ie', 'ї': 'i', 'й': 'i', 'ю': 'iu', 'я': 'ia'}


def create_list_of_word(list_names):
    # создание списка имен
    names = {}
    names.update(list_names[words[0]])
    n = []
    for item in names.values():
        n.append(item)
    return n


def splitting_word_into_letters(data_clean):
    # Раздиление слов на буквы
    separated_words_into_letters = []
    f = str(data_clean)
    # фильтр на комбинацыю символов "зг"

    q = str()
    for w in f:
        print(w)
        if w.find('зг', 0) == -1:
            k = list(w)
        else:
            print(f)
            q = w.replace('зг', '0')
            k = list(q)
            print(q)
        separated_words_into_letters.append(k)

    return separated_words_into_letters


def transmutation_of_word(list_of_words, list_letters):
    # Перевод слов по таблице перевода
    translate_words = [[]] * len(list_of_words)
    n = 0
    for words_list in list_of_words:
        k = []
        for letter in words_list:
            if letter in list_letters:
                words = list_letters[letter.lower()]
                k.append(words)
        conk = ''
        for i in k:
            conk += i
        translate_words[n] = [conk.capitalize()]
        n += 1
    return translate_words


xlsx = pd.read_excel(fn, 0, usecols=words, index_col=None)
data.update(xlsx)

w = splitting_word_into_letters(create_list_of_word(xlsx))
#print(w)
transmutation_of_word(w, letters)

# https://foxford.ru/wiki/informatika/zadachi-poiska-zameny-i-udaleniya-podstroki-v-stroke-v-python
