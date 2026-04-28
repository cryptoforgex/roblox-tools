import json
import requests

class RobloxData:
    BASE_URL = 'https://api.roblox.com/'

    @staticmethod
    def get_game_info(game_id):
        response = requests.get(f'{RobloxData.BASE_URL}games/{game_id}')
        if response.status_code == 200:
            return response.json()
        return None

    @staticmethod
    def search_users(username):
        response = requests.get(f'{RobloxData.BASE_URL}users/get-by-username-json?username={username}')
        if response.status_code == 200:
            return response.json()
        return None

    @staticmethod
    def get_all_assets(user_id, limit=10):
        response = requests.get(f'{RobloxData.BASE_URL}assets?userId={user_id}&limit={limit}')
        if response.status_code == 200:
            return response.json()
        return []

    @staticmethod
    def json_dump(data, file_path):
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)

    @staticmethod
    def json_load(file_path):
        with open(file_path, 'r') as json_file:
            return json.load(json_file)