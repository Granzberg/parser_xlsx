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
    data_list  = creator_lists(list_of_names,choice)

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
a = {'First Name': n,'Last Name': s,'Email Address': e,'Password': password,'Password Hash Function': [],
                   'Org Unit Path': orgUnitPath,'New Primary Email [UPLOAD ONLY]':[],'Status':['Active'],
                   'Last Sign In':[] ,'Recovery Email':[],'Home Secondary Email':[],'Work Secondary Email':[],
                   'Recovery Phone [MUST BE IN THE E.164 FORMAT]':[],'Work Phone':[],'Home Phone':[],'Mobile Phone':[],
                   'Work Address':[],'Home Address':[],'Employee ID':[],'Employee Type':[],'Employee Title':[],
                   'Manager Email':[],'Department':[],'Cost Center':[],'2sv Enrolled [READ ONLY]':[],
                   '2sv Enforced [READ ONLY]':[],'Building ID':[],'Floor Name':[],'Floor Section':[],
                   'Email Usage [READ ONLY]':[],'Drive Usage [READ ONLY]':[],'Total Storage [READ ONLY]':[],
                   'Change Password at Next Sign-In':[],'New Status [UPLOAD ONLY]':[]}
index = len(n)
df = pd.DataFrame.from_dict(a ,orient = index)


df.to_csv(path_or_buf='data.csv',sep=',',index=False, mode='wb')

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