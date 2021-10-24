import pandas as pd

data = {}
data_choice = ['Name_TW', 'Surname_TW', 'Corp_emails']
fn = './translation_names.xlsx'


def creator_lists(name_data, choice):
    names = {}
    names.update(name_data[data_choice[choice]])
    n = []
    for item in names.values():
        n.append(item)
    return n


def names(list_of_names):
    choice = 0
    data_list = creator_lists(list_of_names, choice)

    return data_list


def surnames(list_of_names):
    choice = 1
    data_list = creator_lists(list_of_names, choice)

    return data_list


def emails(list_of_names):
    choice = 2
    data_list = creator_lists(list_of_names, choice)

    return data_list


xlsx = pd.read_excel(fn, 0, usecols=data_choice, index_col=None)
data.update(xlsx)

n = names(data)
s = surnames(data)
e = emails(data)
password = ['22222222'] * len(n)
orgUnitPath = ['/'] * len(n)
status = ['Active'] * len(n)
plug = [''] * len(n)
a = {'First Name': n, 'Last Name': s, 'Email Address': e, 'Password': password, 'Password Hash Function': plug,
     'Org Unit Path': orgUnitPath, 'New Primary Email [UPLOAD ONLY]': plug, 'Status': status, 'Last Sign In': plug,
     'Recovery Email': plug, 'Home Secondary Email': plug, 'Work Secondary Email': plug,
     'Recovery Phone [MUST BE IN THE E.164 FORMAT]': plug, 'Work Phone': plug, 'Home Phone': plug, 'Mobile Phone': plug,
     'Work Address': plug, 'Home Address': plug, 'Employee ID': plug, 'Employee Type': plug, 'Employee Title': plug,
     'Manager Email': plug, 'Department': plug, 'Cost Center': plug, '2sv Enrolled [READ ONLY]': plug,
     '2sv Enforced [READ ONLY]': plug, 'Building ID': plug, 'Floor Name': plug, 'Floor Section': plug,
     'Email Usage [READ ONLY]': plug, 'Drive Usage [READ ONLY]': plug, 'Total Storage [READ ONLY]': plug,
     'Change Password at Next Sign-In': plug, 'New Status [UPLOAD ONLY]': plug}
index = len(n)
df = pd.DataFrame.from_dict(a)


df.to_csv(path_or_buf='data.csv', sep=',', index=False, mode='wb')

#print(df)


# name,surname,email,22222222,,/,,Active,Never logged in,,,,,,,,,,,,,,,,False,False,,,,0.0GB,0.0GB,Unlimited,True,

# ,,,/
# ,,,,/
# Last Sign In ,Recovery Email,Home Secondary Email,Work Secondary Email,/
# Recovery Phone [MUST BE IN THE E.164 FORMAT],Work Phone,Home Phone,Mobile Phone,Work Address,Home Address,/
# Employee ID,Employee Type,Employee Title,Manager Email,Department,Cost Center,2sv Enrolled [READ ONLY],/
# 2sv Enforced [READ ONLY],Building ID,Floor Name,Floor Section,Email Usage [READ ONLY],Drive Usage [READ ONLY],/
# Total Storage [READ ONLY],Change Password at Next Sign-In,New Status [UPLOAD ONLY]

# https://www.edureka.co/community/65139/valueerror-arrays-same-length-valueerror-arrays-same-length