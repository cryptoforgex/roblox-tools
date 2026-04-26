import re

class InputValidator:
    @staticmethod
    def validate_username(username):
        if not isinstance(username, str):
            raise ValueError('Username must be a string')
        if len(username) < 3 or len(username) > 20:
            raise ValueError('Username must be between 3 and 20 characters')
        if not re.match('^[a-zA-Z0-9_]*$', username):
            raise ValueError('Username can only contain alphanumeric characters and underscores')
        return True

    @staticmethod
    def validate_email(email):
        if not isinstance(email, str):
            raise ValueError('Email must be a string')
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(pattern, email):
            raise ValueError('Invalid email format')
        return True

    @staticmethod
    def validate_age(age):
        if not isinstance(age, int) or age < 0:
            raise ValueError('Age must be a non-negative integer')
        return True
