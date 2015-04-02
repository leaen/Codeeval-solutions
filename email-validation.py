import sys
import re

# Define regular expression outside of method to avoid needing to recompile it.
check = re.compile('\w*@\w*.\w*')

def check_email(email):
    if (check.match(email)):
        return True
    return False

with open(sys.argv[1]) as input_file:
    for email in input_file.readlines():
        if (email.strip() == ""):
            continue

        if (check_email(email.strip())):
            print('true')
        else:
            print('false')
