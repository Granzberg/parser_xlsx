import pandas as pd

fn = './translation_names.xlsx'
words = ['Surname_TW', 'Specialty number']
data = {}
print('Create emails....')


def list_of_surnames(raw_data):
    list_surnames = []
    for surnames in raw_data[words[0]]:
        list_surnames.append(surnames)
    return list_surnames


def list_of_specialty_numbers(raw_data):
    list_specialty_numbers = []
    for specialty_numbers in raw_data[words[1]]:
        list_specialty_numbers.append(str(specialty_numbers))
    return list_specialty_numbers


def create_emails(surnames, number):
    emails = []
    for i in range(len(number)):
        if len(number[i]) < 3:
            emails.append(surnames[i].lower() + "_0" + number[i] + '@idguonline.net')
        else:
            emails.append(surnames[i].lower() + "_" + number[i] + '@idguonline.net')
    return emails


xlsx = pd.read_excel(fn, 0, usecols=words, index_col=None)
data.update(xlsx)

surname = list_of_surnames(data)
numbers = list_of_specialty_numbers(data)
emails_list = create_emails(surname, numbers)
print('Creation emails done...')
