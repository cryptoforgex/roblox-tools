import json
import re

class InputValidationError(Exception):
    pass

class Processor:
    def __init__(self):
        self.valid_inputs = []

    def validate_input(self, user_input):
        if not isinstance(user_input, str):
            raise InputValidationError("Input must be a string.")
        if len(user_input) == 0:
            raise InputValidationError("Input cannot be empty.")
        if not re.match(r'^[a-zA-Z0-9_]+$', user_input):
            raise InputValidationError("Input must be alphanumeric and underscores only.")
        self.valid_inputs.append(user_input)

    def process_inputs(self, inputs):
        for user_input in inputs:
            try:
                self.validate_input(user_input)
            except InputValidationError as e:
                print(f'Invalid input: {e}')
                continue
            print(f'Processing: {user_input}')  

if __name__ == '__main__':
    processor = Processor()
    inputs = ['valid_input1', 'invalid input!', '12345', '']
    processor.process_inputs(inputs)
