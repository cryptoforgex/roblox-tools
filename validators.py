import re

def validate_username(username):
    return bool(re.match(r'^[a-zA-Z0-9_]{3,20}$', username))


def validate_password(password):
    return (len(password) >= 8 and 
            re.search(r'[A-Za-z]', password) and 
            re.search(r'[0-9]', password))


def validate_email(email):
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(regex, email))


def validate_age(age):
    return isinstance(age, int) and 0 < age < 150


def validate_data(username, password, email, age):
    return (validate_username(username) and 
            validate_password(password) and 
            validate_email(email) and 
            validate_age(age))