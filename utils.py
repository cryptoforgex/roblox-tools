import json
import requests

class RobloxAPI:
    BASE_URL = 'https://api.roblox.com/'

    @staticmethod
    def fetch_user_info(user_id):
        response = requests.get(f'{RobloxAPI.BASE_URL}users/{user_id}')
        if response.status_code == 200:
            return response.json()
        raise ValueError('User not found')

    @staticmethod
    def fetch_game_info(game_id):
        response = requests.get(f'{RobloxAPI.BASE_URL}games/{game_id}')
        if response.status_code == 200:
            return response.json()
        raise ValueError('Game not found')

    @staticmethod
    def save_to_json(data, filename):
        with open(filename, 'w') as json_file:
            json.dump(data, json_file, indent=4)

    @staticmethod
    def read_from_json(filename):
        with open(filename, 'r') as json_file:
            return json.load(json_file)