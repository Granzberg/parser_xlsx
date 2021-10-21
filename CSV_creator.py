import pandas as pd
import translation_words as tw

data = {}
data_choice = ['patronymic', 'spec', 'corp']
fn = './fuaid.xlsx'
print('Create xlsx file .....')


def create_list_of_names(list_names):
    # создание списка (0 - имена, 1 - специальности, 2 - корп.почта)
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
    return data_clean


def surname_str(name_s):
    # возврат списка фамилий
    k = 1
    surname = create_words(name_s, k)
    return surname


def names_str(name_s):
    # возврат списка имен
    k = 0
    names = create_words(name_s, k)
    return names


def create_words(names, k):
    # создание списка
    j = []
    for i in names[0]:
        j.append(i)
    j = [item.split() for item in j]
    l = len(j)
    names_list = []

    for n in range(0, l):
        # k примает переданое занчение из функции и тем самым происходит раздиление по назначению..
        if k == 1:
            for i in j[n][1:2]:
                names_list.append(i)
        else:
            for i in j[n][:1]:
                names_list.append(i)
    return names_list


def cor_email(corp_email1):
    # создание корп. почты
    emails = []
    for em in corp_email1[2]:
        emails.append(em)
    return emails


def spec_number(spec):
    # создание списка с кодом специальности
    c = []
    for u in spec[1]:
        c.append(u)
    c = [item.split() for item in c]
    l = len(c)
    spec_num = []
    for n in range(0, l):
        for i in c[n][:1]:
            spec_num.append(i)
    return spec_num


# Чтение исходного файла xlsx
xlsx = pd.read_excel(fn, 0, usecols=data_choice, index_col=None)
data.update(xlsx)

# Создание выборки после парсинга xlsx
list_of_names = create_list_of_names(xlsx)
Name_TW = tw.name_tw
Surname_TW = tw.surname_tw
index = []
for i in range(len(names_str(list_of_names))):
    index.append(i)
#print(index)

# write to Excel
df1 = pd.DataFrame({'Name': names_str(list_of_names),
                   'Surname': surname_str(list_of_names),
                    'Name_TW': Name_TW,
                    'Surname_TW': Surname_TW,
                    'Specialty number': spec_number(list_of_names),
                    'Corp_emails': cor_email(list_of_names)},
                   index=index)
with pd.ExcelWriter('./translation_names.xlsx') as writer:
    df1.to_excel(writer, sheet_name="Sheet1", index_label="№", merge_cells=False)

csv = pd.DataFrame()
print('Xlsx file done ...')
# name,surname,email,22222222,,/,,Active,Never logged in,,,,,,,,,,,,,,,,False,False,,,,0.0GB,0.0GB,Unlimited,True,

# First Name,Last Name,Email Address,Password ,/
# Password Hash Function [UPLOAD ONLY],Org Unit Path [Required],New Primary Email [UPLOAD ONLY],Status,/
# Last Sign In ,Recovery Email,Home Secondary Email,Work Secondary Email,/
# Recovery Phone [MUST BE IN THE E.164 FORMAT],Work Phone,Home Phone,Mobile Phone,Work Address,Home Address,/
# Employee ID,Employee Type,Employee Title,Manager Email,Department,Cost Center,2sv Enrolled [READ ONLY],/
# 2sv Enforced [READ ONLY],Building ID,Floor Name,Floor Section,Email Usage [READ ONLY],Drive Usage [READ ONLY],/
# Total Storage [READ ONLY],Change Password at Next Sign-In,New Status [UPLOAD ONLY]
