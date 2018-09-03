import re

def validate_name(name):
    match = re.search(r'^[a-zA-Z_]\w{3,}', name)
    match2 = re.search(r'\W+$', name)
    if match and not match2:
        print "Valid name", name
    else:
        print "not a valid ", name

validate_name(raw_input("Enter the variable to be validated:"))
