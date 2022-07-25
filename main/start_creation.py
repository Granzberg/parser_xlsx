import pandas as pd

data = {}
data_choice = ['patronymic', 'spec']
fn = '..//test/test.xlsx'
print('Create xlsx file .....')


def create_list_of_names(list_names):   # creating a list (0 - names, 1 - specialties, 2 - corporate mail)
    names = {}
    data_clean = []
    names.update(list_names[data_choice[0]])    # separates names from the general raw list
    clean_name = []
    for item in names.values():
        clean_name.append(item)
    spec = {}
    spec.update(list_names[data_choice[1]])     # separates specialties from the general raw list
    clean_specialties = []
    for item in spec.values():
        clean_specialties.append(item)

    data_clean.append(clean_name)
    data_clean.append(clean_specialties)
    return data_clean


def surname_str(name_s):    # return list of last names
    list_of_last_names = 0
    surname = create_words(name_s, list_of_last_names)
    return surname


def names_str(name_s):      # return a list of names
    list_of_names0 = 1
    names = create_words(name_s, list_of_names0)
    return names


def create_words(names, k):     # creating a list of words
    new_list = []
    for i in names[0]:
        new_list.append(i)
    divided_by_words = [item.split() for item in new_list]     # separating into list of words from names
    list_length = len(divided_by_words)  # length of list of separated words
    names_list = []

    for n in range(0, list_length):     # 'k' accepts the passed value from the function and thus separates according to purpose
        if k == 1:
            for i in divided_by_words[n][1:2]:  # filling list with names
                names_list.append(i)
        else:
            for i in divided_by_words[n][:1]:   # filling in the list with names
                names_list.append(i)
    return names_list


def spec_number(spec):      # creating a list with a specialty code
    numbers_of_cp = []
    for u in spec[1]:       # obtaining a specialty number by index
        numbers_of_cp.append(u)     # adding the received value to the general list
    numbers_of_cp = [item.split() for item in numbers_of_cp]    # division of the list into specialty number and specialty name
    number_of_specialty_numbers = len(numbers_of_cp)
    spec_num = []
    for n in range(0, number_of_specialty_numbers):
        for i in numbers_of_cp[n][:1]:      # getting a specialty number from the list
            spec_num.append(i)
    return spec_num


xlsx = pd.read_excel(fn, 0, usecols=data_choice, index_col=None)    # Reading xlsx source file
data.update(xlsx)

list_of_names = create_list_of_names(xlsx)
# variable for transferring processed information to another file
names_str = names_str(list_of_names)
surname_str = surname_str(list_of_names)
spec_number = spec_number(list_of_names)

df1 = pd.DataFrame({'Name': names_str,
                    'Surname': surname_str,
                    'Specialty number': spec_number})

with pd.ExcelWriter('../test/translation_names.xlsx') as writer:
    df1.to_excel(writer, sheet_name="Sheet1", index_label="№")

print('Xlsx file done ...')
