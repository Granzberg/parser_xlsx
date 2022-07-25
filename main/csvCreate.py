import pandas as pd
import translation as tw
import ccEmail as cce

pas = 'yourPass'         # here you can enter the initial password (you need eight characters)
unitPath = '/'           # here you can bind mail to a group after '/'

# data to write to CSV file
name = tw.name_tw
surname = tw.surname_tw
emails = cce.emails_list
print('csv create ....')
password = [pas] * len(name)
orgUnitPath = [unitPath] * len(name)
plug = [''] * len(name)                    # the necessary stub for creating mail (do not change in any way)
# the minimum required information to create corporate mail in Google Workspace
a = {'First Name': name, 'Last Name': surname, 'Email Address': emails, 'Password': password, 'Password Hash Function': plug,
     'Org Unit Path': orgUnitPath, 'New Primary Email [UPLOAD ONLY]': plug, 'Recovery Email': plug,
     'Home Secondary Email': plug, 'Work Secondary Email': plug,
     'Recovery Phone [MUST BE IN THE E.164 FORMAT]': plug, 'Work Phone': plug, 'Home Phone': plug, 'Mobile Phone': plug,
     'Work Address': plug, 'Home Address': plug, 'Employee ID': plug, 'Employee Type': plug, 'Employee Title': plug,
     'Manager Email': plug, 'Department': plug, 'Cost Center': plug, '2sv Enrolled [READ ONLY]': plug,
     '2sv Enforced [READ ONLY]': plug, 'Building ID': plug, 'Floor Name': plug, 'Floor Section': plug,
     'Email Usage [READ ONLY]': plug, 'Drive Usage [READ ONLY]': plug, 'Total Storage [READ ONLY]': plug,
     'Change Password at Next Sign-In': plug, 'New Status [UPLOAD ONLY]': plug}
index = len(name)
df = pd.DataFrame.from_dict(a)

df.to_csv(path_or_buf='../test/data.csv', sep=',', index=False, mode='wb')
print('csv done....')
