import pandas as pd
data = {}
data_choice = ['patronymic', 'spec', 'corp']
fn = './fuaid.xlsx'

xlsx = pd.read_excel(fn, 0, usecols=data_choice, index_col=None)
data.update(xlsx)


def create_list_of_names(list_names):
    # создание списка на выбор 'data_choice'(0 - имена, 1 - специальности, 2 - корп.почта)
    names = {}
    data_clean = []
    names.update(list_names[data_choice[0]])
    n = []
    for item in names.values():
        n.append(item)
    spec = {}
    spec.update(list_names[data_choice[1]])
    sp = []
    for item in spec.values():
        sp.append(item)
    corp = {}
    corp.update(list_names[data_choice[2]])
    e = []
    for item in corp.values():
        e.append(item)
    data_clean.append(n)
    data_clean.append(sp)
    data_clean.append(e)
    #print(data_clean)
    return data_clean


def surname_str(name_s):
    # создание списка фамилий
    surname = []
    for u in name_s[0]:
        surname.append(u)
    surname = [[item] for item in surname]
    print(surname)
    return surname


def names_str(name_s):
    # создание списка имен
    names = []
    for i in name_s:
        names.append(i[1:2])
    return names


# def corporate_emails(list_names):
#     # создание списка почты
#     emails = []
#     corp_email = []
#     emails.append(list_names[data_choice[2]])
#     emails = list(emails)
#     length = len(emails)
#     for i in range(length):
#         corp_email.append(emails[i])
#     return corp_email


def cor_email(corp_email1):
    # создание корп. почты
    emails = []
    for em in corp_email1:
        emails.append(em)
    return emails

# choice = int(input('Какие данные нужны?(0, 1, 2): '))
# choice = 2


list_of_names = create_list_of_names(xlsx)
#list_of_corp_email = corporate_emails(xlsx)
s = surname_str(list_of_names)
#print(s)
#print(list_of_names)
#print(list_of_corp_email)



# write to Excel
# df = pd.DataFrame({'Name': names_str(list_of_names),
#                    'Surname': surname_str(list_of_names),
#                    'Corp_emails': cor_email(list_of_corp_email)})
# with pd.ExcelWriter('./test.xlsx') as writer:
#     df.to_excel(writer, sheet_name="Sheet1")
