import pandas as pd

fn = './test.xlsx'
words = ['Name', 'Surname']
data = {}

letters = {'а': 'a', 'б': 'd', 'в': 'v', 'г': 'h', 'ґ': 'g', 'д': 'd', 'е': 'e', 'є': 'ye', 'ж': 'zh', 'з': 'z',
           'и': 'y', 'і': 'i', 'ї': 'yi', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
           'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'kh', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ю': 'yu', 'я': 'ya',
           '0': 'zgh'}

alternate_letters = {'є': 'ie', 'ї': 'i', 'й': 'i', 'ю': 'iu', 'я': 'ia'}
print('Translation of words is in progress .....')


def create_list_of_names(list_names):
    # создание списка имен
    names = {}
    names.update(list_names[words[1]])
    n = []
    for item in names.values():
        n.append(item)
    return n


def create_list_of_surname(list_names):
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
    # Перевод слов по основной таблице перевода
    translate_words = [[]] * len(list_of_words)
    n = 0

    for words_list in list_of_words:
        test0 = first_filter(words_list, second_filter)
        test = filter_second(test0)
        k = []

        for letter in test:
            if letter.lower() in list_letters:
                words = list_letters[letter.lower()]
                k.append(words)
            else:
                k.append(letter.lower())
        conk = ''
        for i in k:
            conk += i
        translate_words[n] = conk.capitalize()
        n += 1
    return translate_words


def first_filter(words_list, second_filter):
    # замена букв по альтернативной таблице перевода
    h = []
    list_after_processing = []
    for w in words_list:
        if w in second_filter:
            h = second_filter[w]
            list_after_processing.append(h)
        else:
            list_after_processing.append(w)
    return list_after_processing


def filter_second(words_list):
    # удаление апострофа и мягкого знака
    second_filter = ["'", 'ь']
    list_after_second_processing = []
    for w in words_list:
        if w in second_filter:
            list_after_second_processing.append(w)
            if w == "'":
                list_after_second_processing.remove("'")
            else:
                list_after_second_processing.remove('ь')
        else:
            list_after_second_processing.append(w)
    return list_after_second_processing


xlsx = pd.read_excel(fn, 0, usecols=words, index_col=None)
data.update(xlsx)


n = splitting_word_into_letters(create_list_of_names(xlsx))
s = splitting_word_into_letters(create_list_of_surname(xlsx))

# write to Excel
name_tw = transmutation_of_word(n, letters, alternate_letters)
surname_tw = transmutation_of_word(s, letters, alternate_letters)
# df2 = pd.DataFrame({'Name': transmutation_of_word(n, letters, alternate_letters),
#                    'Surname': transmutation_of_word(s, letters, alternate_letters),
#                    })
# with pd.ExcelWriter('./translation_names.xlsx') as writer:
#     df2.to_excel(writer, sheet_name="Sheet2", index_label="№", merge_cells=False)
# csv = pd.DataFrame()
print('Translation done ...')
