import json

class ConfigLoader:
    def __init__(self, default_config):
        self.config = default_config

    def load(self, filename):
        try:
            with open(filename, 'r') as file:
                user_config = json.load(file)
                self.config.update(user_config)
        except FileNotFoundError:
            pass
        except json.JSONDecodeError:
            print('Invalid JSON format in config file.')

    def get(self, key, default=None):
        return self.config.get(key, default)

if __name__ == '__main__':
    default_config = {
        'setting1': 'default_value1',
        'setting2': 'default_value2',
    }
    config_loader = ConfigLoader(default_config)
    config_loader.load('config.json')
    print(config_loader.get('setting1'))
