#! python3
# phoneAndEmail.py - Находит телефонные номера и адреса электронной почты в буфере обмена.

import pyperclip, re

phoneRegex = re.compile(r'\d{10}|\d{12}')

# Создание регулярноого выражения для адресов электронной почты.
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+                       # имя пользователя
    @                                       # символ @
    [a-zA-Z9.-]+                            # имя домена
    (\.[a-zA-Z]{2,4})                       # остальная часть адреса
    )''', re.VERBOSE)

# Поиск соотвецтвийв тексте фаимилии, имени.
nameRegex = re.compile('[А-Яа-я]{3,}')

# Поиск соотвецтвий в тексте, содежащемся в буфере обмена.
text = str(pyperclip.paste())
matches = []
phones = []
for groups in phoneRegex.findall(text):
    phones.append(groups)
email = []
for groups in emailRegex.findall(text):
    email.append(groups[0])
name = []
for groups in nameRegex.findall(text):
    name.append(groups)

matches.append(str(name))
matches.append(str(phones))
matches.append(str(email))

# Копирование результатов в буфер обмена.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Скопировано в буфер обмена')
    print(matches)
else:
    print('Что-то не так!')

