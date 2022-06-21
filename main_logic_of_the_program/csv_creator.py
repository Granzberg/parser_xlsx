import pandas as pd
import translation_words as tw
import create_corporate_email as cce


# data to write to CSV file
n = tw.name_tw
s = tw.surname_tw
e = cce.emails_list

password = ['22222222'] * len(n)        # creates a list of identical passwords equal
                                        # to the length of the resulting list of names'n'
orgUnitPath = ['/'] * len(n)            # creates a list equal to the length of the resulting list of names
plug = [''] * len(n)                    # creates a list of empty strings equal to the length
                                        # of the resulting list of names
# the minimum required information to create corporate mail in Google Workspace
a = {'First Name': n, 'Last Name': s, 'Email Address': e, 'Password': password, 'Password Hash Function': plug,
     'Org Unit Path': orgUnitPath, 'New Primary Email [UPLOAD ONLY]': plug, 'Recovery Email': plug,
     'Home Secondary Email': plug, 'Work Secondary Email': plug,
     'Recovery Phone [MUST BE IN THE E.164 FORMAT]': plug, 'Work Phone': plug, 'Home Phone': plug, 'Mobile Phone': plug,
     'Work Address': plug, 'Home Address': plug, 'Employee ID': plug, 'Employee Type': plug, 'Employee Title': plug,
     'Manager Email': plug, 'Department': plug, 'Cost Center': plug, '2sv Enrolled [READ ONLY]': plug,
     '2sv Enforced [READ ONLY]': plug, 'Building ID': plug, 'Floor Name': plug, 'Floor Section': plug,
     'Email Usage [READ ONLY]': plug, 'Drive Usage [READ ONLY]': plug, 'Total Storage [READ ONLY]': plug,
     'Change Password at Next Sign-In': plug, 'New Status [UPLOAD ONLY]': plug}
index = len(n)
df = pd.DataFrame.from_dict(a)

df.to_csv(path_or_buf='..//processed_data/data.csv', sep=',', index=False, mode='wb')
print('csv create done....')
