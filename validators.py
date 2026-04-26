import re

def validate_username(username):
    if not isinstance(username, str) or len(username) < 3 or len(username) > 20:
        return False
    return re.match(r'^[A-Za-z0-9_]+$', username) is not None


def validate_password(password):
    if not isinstance(password, str) or len(password) < 8:
        return False
    return any(char.isdigit() for char in password) and any(char.isalpha() for char in password)


def validate_input(username, password):
    username_valid = validate_username(username)
    password_valid = validate_password(password)
    return username_valid, password_valid