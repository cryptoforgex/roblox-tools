import json
import requests

class RobloxAPIError(Exception):
    pass

def fetch_roblox_data(endpoint):
    url = f'https://api.roblox.com/{endpoint}'
    response = requests.get(url)
    if response.status_code != 200:
        raise RobloxAPIError(f'Error fetching data: {response.status_code}')
    return response.json()

def parse_user_data(user_data):
    return {
        'username': user_data.get('name'),
        'user_id': user_data.get('id'),
        'avatar_url': user_data.get('avatar'),
    }

def get_user_info(user_id):
    user_data = fetch_roblox_data(f'users/{user_id}')
    return parse_user_data(user_data)