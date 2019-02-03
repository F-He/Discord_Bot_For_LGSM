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
    
    def get_bot_embed_color(self):
        return int(self._config["general_settings"]["bot_embed_color"], 16)
    
    def get_commands_with_description(self):
        return self._config._sections["command_descriptions"]
    
    def get_switch_server_cooldown(self):
        return self._config["general_settings"]["switch_server_cooldown"]