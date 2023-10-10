import re
def is_acceptable_password(password: str) -> bool:
    unique_chars = set(re.findall(r'[a-zA-Z0-9]', password))
    if len(unique_chars)<3:
        return False
    elif "password" in password.lower():
        return False
    elif len(password) > 9:
        return True
    elif str.isnumeric(password):
        return False
    elif len(password) > 6:        
        for i in password:
            if str.isdigit(i):
                return True
            
    return False
