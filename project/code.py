"""
This module defines a function to check the acceptability of a password.
"""
import re
def is_acceptable_password(password: str) -> bool:
    """
    Check if a password is acceptable based on a specific criteria.
    Args:
        password (str): The password to be checked.
    Returns:
        bool: True if the password is acceptable, False otherwise.
        """
    unique_chars = set(re.findall(r'[a-zA-Z0-9]', password))
    if len(unique_chars)<3:
        return False
    if "password" in password.lower():
        return False
    if len(password) > 9:
        return True
    if str.isnumeric(password):
        return False
    if len(password) > 6:
        for i in password:
            if str.isdigit(i):
                return True
    return False
