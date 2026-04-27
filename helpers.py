import json

def load_json_file(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)

def save_json_file(filepath, data):
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)

def merge_json_data(base_data, new_data):
    base_data.update(new_data)
    return base_data

def extract_field(data, field):
    return data.get(field, None)

def filter_data(data, condition):
    return {key: value for key, value in data.items() if condition(key, value)}
