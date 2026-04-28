import json

def load_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def save_data(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def get_player_data(players, player_id):
    return players.get(player_id, None)


def update_player_data(players, player_id, player_info):
    players[player_id] = player_info


def remove_player_data(players, player_id):
    if player_id in players:
        del players[player_id]


def filter_active_players(players):
    return {pid: info for pid, info in players.items() if info.get('active', False)}
