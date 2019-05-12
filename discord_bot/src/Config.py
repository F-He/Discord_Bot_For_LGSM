import configparser
from src.Utils import convert_str_to_hex


class Config(object):
    def __init__(self, config_path: str):
        self._config_path = config_path
        self._config = configparser.ConfigParser()
        self._config.read(self._config_path)

    def reload_config(self):
        self._config.read(self._config_path)

    def get_token(self):
        return self._config["general_settings"]["bot_token"]

    def get_command_prefix(self):
        return self._config["general_settings"]["command_prefix"]

    def get_bot_status(self):
        return self._config["general_settings"]["bot_status"]

    def get_command_aliases_for(self, command_name: str):
        return str(self._config["command_aliases"][command_name]).split(",")

    def get_bot_embed_color(self):
        return convert_str_to_hex(self._config["general_settings"]["bot_embed_color"])

    def get_commands_with_description(self):
        return self._config._sections["command_descriptions"]

    def get_start_server_cooldown(self):
        return self._config.getint("command_settings", "start_server_cooldown")

    def get_stop_server_cooldown(self):
        return self._config.getint("command_settings", "stop_server_cooldown")

    def server_exists(self, server_name):
        if server_name not in self._config["game_servers"]:
            return False
        else:
            return True

    def get_server_file_path(self, server_name):
        return self._config["game_servers"][server_name]

    def get_all_servers(self):
        return self._config["game_servers"]

    def get_role_for_executing_command(self, command_name):
        return self._config["command_settings"][command_name]

    def check_if_server_specified(self, server_name):
        return self._config.has_option("game_servers", server_name)

    def is_parallel_running_allowed(self):
        return self._config.getboolean("general_settings", "allow_parallel_running")

    def get_max_parallel_running_count(self):
        return self._config.getint("general_settings", "max_parallel_running_count")
