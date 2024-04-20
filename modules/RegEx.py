import re

def regexCheck(pattern, text):
    if re.fullmatch(pattern, text):
        return True
    else:
        return False

def passwordCheck(password):
    return regexCheck('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*(),.?":{}|<>])[a-zA-Z\d!@#$%^&*(),.?":{}|<>]{8,20}$', password)

print(passwordCheck("zoo@123456ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZz"))
