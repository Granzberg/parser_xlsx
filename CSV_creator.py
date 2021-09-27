import pandas as pd
data = {}
data_choice = ['patronymic', 'spec', 'corp']
fn = './fuaid.xlsx'

xlsx = pd.read_excel(fn, 0, usecols=data_choice, index_col=None)
data.update(xlsx)


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
    # создание списка фамилий
    g = []
    for u in name_s[0]:
        g.append(u)
    g = [item.split() for item in g]
    l = len(g)
    surname = []
    for n in range(0,l):
        for i in g[n][:1]:
            surname.append(i)
    return surname


def names_str(name_s):
    # создание списка имен
    j = []
    for i in name_s[0]:
        j.append(i)
    j = [item.split() for item in j]
    l = len(j)
    names = []
    for n in range(0,l):
        for i in j[n][1:2]:
            names.append(i)
    return names


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

# Создание выборки после парсинга xlsx
list_of_names = create_list_of_names(xlsx)

# write to Excel
df = pd.DataFrame({'Name': names_str(list_of_names),
                   'Surname': surname_str(list_of_names),
                   'Specialty number': spec_number(list_of_names),
                   'Corp_emails': cor_email(list_of_names)})
with pd.ExcelWriter('./test.xlsx') as writer:
    df.to_excel(writer, sheet_name="Sheet1")
print('Done')
