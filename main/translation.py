import secondStep as start

# transliteration from Ukrainian into Latin alphabet
letters = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'h', 'ґ': 'g', 'д': 'd', 'е': 'e', 'є': 'ye', 'ж': 'zh', 'з': 'z',
           'и': 'y', 'і': 'i', 'ї': 'yi', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
           'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'kh','ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ю': 'yu', 'я': 'ya',
           '0': 'zgh'}
# alternative translation table
alternate_letters = {'є': 'ie', 'ї': 'i', 'й': 'i', 'ю': 'iu', 'я': 'ia'}
print('Translation of words is in progress .....')


def splitting_word_into_letters(data_clean):        # Splitting words into letters
    separated_words_into_letters = []
    # character combination filter "зг"
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


def transmutation_of_word(list_of_words, list_letters, second_filter):      # Translation of words according to the
                                                                            # main translation table
    translate_words = [[]] * len(list_of_words)     # creates empty lists by length of list of names
                                                                            # to replace by list index
    n = 0
    for words_list in list_of_words:        # splits names into letters
        test0 = alternative_filter(words_list, second_filter)     # checking for letters from an alternative dictionary
        test = filter_second(test0)         # removing apostrophe and soft sign from list of letters
        k = []

        for letter in test:         # letter transliteration using basic transliteration
            if letter.lower() in list_letters:      # Changing letter case to cute
                words = list_letters[letter.lower()]
                k.append(words)
            else:
                k.append(letter.lower())
        conk = ''
        for i in k:
            conk += i       # letter-by-letter concatenation with an empty string
        translate_words[n] = conk.capitalize()
        n += 1
    return translate_words


def alternative_filter(words_list, second_filter):          # replacement of letters according to the
                                                            # alternative translation table
    list_after_processing = []
    for w in words_list:
        if w in second_filter:
            h = second_filter[w]
            list_after_processing.append(h)
        else:
            list_after_processing.append(w)
    return list_after_processing


def filter_second(words_list):  # remove apostrophe and soft sign
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


# variable for transferring processed information to another file
name_tw = transmutation_of_word(start.names, letters, alternate_letters)
surname_tw = transmutation_of_word(start.surname, letters, alternate_letters)

print('Translation done ...')
