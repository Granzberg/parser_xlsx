import secondStep as start
import translation as tw

data = {}
domain = '@your.domain'
print('Create emails....')


def create_emails(surnames, number, your_domain):   # creation of an email based on the received names and numbers of specialists from other files
    emails = []
    for i in range(len(number)):
        if len(number[i]) < 3:      # if the specialty number is shorter than 3 characters, then a 0 character is added before it
            emails.append(surnames[i].lower() + "_0" + str(number[i]) + your_domain)
        else:
            emails.append(surnames[i].lower() + "_" + str(number[i]) + your_domain)
    return emails


surname = tw.surname_tw
numbers = start.spec_number
# variable for transferring processed information to another file
emails_list = create_emails(surname, numbers, domain)
print('Creation emails done...')
