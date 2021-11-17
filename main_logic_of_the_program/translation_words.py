import start_creation as start

data = {}

letters = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'h', 'ґ': 'g', 'д': 'd', 'е': 'e', 'є': 'ye', 'ж': 'zh', 'з': 'z',
           'и': 'y', 'і': 'i', 'ї': 'yi', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
           'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'kh','ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ю': 'yu', 'я': 'ya',
           '0': 'zgh'}

alternate_letters = {'є': 'ie', 'ї': 'i', 'й': 'i', 'ю': 'iu', 'я': 'ia'}
print('Translation of words is in progress .....')


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
    second_filter = ["’", 'ь']
    list_after_second_processing = []
    for w in words_list:
        if w in second_filter:
            list_after_second_processing.append(w)
            if w == "’":
                list_after_second_processing.remove("’")
            else:
                list_after_second_processing.remove('ь')
        else:
            list_after_second_processing.append(w)
    return list_after_second_processing


# write to Excel
name_tw = transmutation_of_word(start.names_str, letters, alternate_letters)
surname_tw = transmutation_of_word(start.surname_str, letters, alternate_letters)

print('Translation done ...')
