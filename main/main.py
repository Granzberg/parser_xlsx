import translation as tw
import ccEmail as cce
import secondStep as start
import csvCreate as csv

# transferring data from other program files
if __name__ == '__main__':
    names_str = start.names_str
    surname_str = start.surname_str
    name_TW = tw.name_tw
    surname_TW = tw.surname_tw
    spec_number = start.spec_number
    emails = cce.emails_list
    fail = csv.df
