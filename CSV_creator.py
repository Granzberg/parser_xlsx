import pandas as pd
data = {}
data_choice = ['patronymic', 'spec', 'corp']


xlsx = pd.read_excel('./fuaid.xlsx',sheet_name='Sheet1',usecols=['patronymic','spec','corp'])
data.update(xlsx)

# создание списка на выбор 'data_choice'(0 - имена, 1 - специальности, 2 - корп.почта)
def create_list_of_names(list_names):
    names = set()
    name = []
    names.update(data[data_choice[0]])
    names = list(names)
    length = len(names)
    for i in range(length):
        h = names[i].split()
        name.append(h)
    return name

# создание списка имен
def names_str(name_s):
    for name_l in list_of_names:
        name_1 = str(name_l[0])
        return name_1


# создание списка фамилий
def surname_str(name_s):
    for name_l in list_of_names:
        surname = str(name_l[1])
        return surname

# создание списка почты(в процессе)
def corporate_emails(list_names):
    emails = set()
    corp_email = []
    emails.update(data[data_choice[2]])
    emails = list(emails)
    length = len(emails)
    for i in range(length):
        h = emails[i].split()
        corp_email.append(h)

    return corp_email

def cor_email(corp_email):
    for em in corp_email:
        email = str(em)
        return email

#choice = int(input('Какие данные нужны?(0, 1, 2): '))
#choice = 2
list_of_names = create_list_of_names(xlsx)

list_of_corp_email = corporate_emails(xlsx)

# write to Excel
df = pd.DataFrame({'Name':[names_str(list_of_names)],
                   'Surname':[surname_str(list_of_names)],
                   'Corp_emails':[cor_email(list_of_corp_email)]})
with pd.ExcelWriter('./test.xlsx') as writer:
    df.to_excel(writer, sheet_name="Sheet1")