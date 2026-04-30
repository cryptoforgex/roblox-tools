import re

def validate_username(username):
    if not isinstance(username, str) or len(username) < 3:
        raise ValueError('Username must be a string with at least 3 characters')
    if not re.match('^[a-zA-Z0-9_]*$', username):
        raise ValueError('Username can only contain letters, numbers, and underscores')


def validate_password(password):
    if not isinstance(password, str) or len(password) < 6:
        raise ValueError('Password must be a string with at least 6 characters')
    if re.search('[ ]', password):
        raise ValueError('Password cannot contain spaces')


def validate_email(email):
    if not isinstance(email, str) or not re.match(r'^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}$', email):
        raise ValueError('Invalid email format')
