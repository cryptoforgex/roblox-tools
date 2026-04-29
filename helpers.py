import json

def load_roblox_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def save_roblox_data(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def update_roblox_data(file_path, new_data):
    data = load_roblox_data(file_path)
    data.update(new_data)
    save_roblox_data(file_path, data)

def delete_roblox_entry(file_path, key):
    data = load_roblox_data(file_path)
    data.pop(key, None)
    save_roblox_data(file_path, data)