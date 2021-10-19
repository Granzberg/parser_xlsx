import pandas as pd

fn = './test.xlsx'
words = ['Name', 'Surname']
data = {}

letters = {'а': 'a', 'б': 'd', 'в': 'v', 'г': 'h', 'ґ': 'g', 'д': 'd', 'е': 'e', 'є': 'ye', 'ж': 'zh', 'з': 'z',
           'и': 'y', 'і': 'i', 'ї': 'yi', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'р': 'r',
           'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'kh', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ю': 'yu', 'я': 'ya',
           '0': 'zgh'}

alternate_letters = {'є': 'ie', 'ї': 'i', 'й': 'i', 'ю': 'iu', 'я': 'ia'}


def create_list_of_names(list_names):
    # создание списка имен
    names = {}
    names.update(list_names[words[0]])
    n = []
    for item in names.values():
        n.append(item)
    return n


def create_list_of_surname(list_names):
    # создание списка имен
    names = {}
    names.update(list_names[words[1]])
    n = []
    for item in names.values():
        n.append(item)
    return n


def splitting_word_into_letters(data_clean):
    # Раздиление слов на буквы
    separated_words_into_letters = []
    # фильтр на комбинацыю символов "зг"
    k = ''
    for w in data_clean:
        if w.find('зг', 0) == -1:
            k = list(w)
            separated_words_into_letters.append(k)
        else:
            q = w.replace('зг', '0')
            k = list(q)
            separated_words_into_letters.append(k)

    return separated_words_into_letters


def transmutation_of_word(list_of_words, list_letters, second_filter):
    # Перевод слов по таблице перевода
    translate_words = [[]] * len(list_of_words)
    n = 0
    # Работает не правильно ...
    # походу требуется разбить на болие мелкие функции и использввать их как методы в нутри этой
    for words_list in list_of_words:
        h = []
        test = []
        k = []
        for w in words_list:
            if w in second_filter:
                h = second_filter[w]
                test.append(h)
            else:
                test.append(w)
                for letter in test:
                    if letter.lower() in list_letters:
                        words = list_letters[letter.lower()]
                        k.append(words)
        conk = ''
        for i in k:
            conk += i
        translate_words[n] = [conk.capitalize()]
        n += 1
    print(translate_words)
    # return translate_words



xlsx = pd.read_excel(fn, 0, usecols=words, index_col=None)
data.update(xlsx)

#rint(xlsx)
n = splitting_word_into_letters(create_list_of_names(xlsx))
transmutation_of_word(n, letters, alternate_letters)
#
# s = splitting_word_into_letters(create_list_of_surname(xlsx))
# surname = transmutation_of_word(s, letters, alternate_letters)

# print('*************************************')
# print(surname)