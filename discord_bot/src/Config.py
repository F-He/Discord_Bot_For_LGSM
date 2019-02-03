import configparser


class Config(object):
    def __init__(self, configPath: str):
        self._configPath = configPath
        self._config = configparser.ConfigParser()
        self._config.read(self._configPath)
    
    def get_token(self):
        return self._config["general_settings"]["bot_token"]
    
    def get_command_prefix(self):
        return self._config["general_settings"]["command_prefix"]
    
    def get_bot_status(self):
        return self._config["general_settings"]["bot_status"]
    
    def get_command_aliases_for(self, command_name: str):
        return str(self._config["command_aliases"][command_name]).split(",")