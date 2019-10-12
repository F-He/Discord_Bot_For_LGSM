import base64
import configparser
from src.Utils import convert_str_to_hex

default_config = "W2dlbmVyYWxfc2V0dGluZ3NdCmJvdF90b2tlbiA9IFRPS0VOX0hFUkUKYm90X3N0YXR1cyA9ICFoZWxwIGZvciBpbmZvcwpjb21tYW5kX3ByZWZpeCA9ICEKCjsgTmVlZHMgdG8gYmUgYSBIZXggdmFsdWUuCmJvdF9lbWJlZF9jb2xvciA9ICM1NDdlMzQKCjsgU3BlY2lmeSBpZiBhbmQgaG93IG1hbnkgZ2FtZSBzZXJ2ZXJzIGNhbiBydW4gYXQgdGhlIHNhbWUgdGltZS4KYWxsb3dfcGFyYWxsZWxfcnVubmluZyA9IFRydWUKbWF4X3BhcmFsbGVsX3J1bm5pbmdfY291bnQgPSAxCgoKW2NvbW1hbmRfc2V0dGluZ3NdCjsgQ29vbGRvd24gdGltZSBpbiBzZWNvbmRzIGJldHdlZW4gc2VydmVyIGNvbW1hbmRzLgpzdGFydF9zZXJ2ZXJfY29vbGRvd24gPSAzMApzdG9wX3NlcnZlcl9jb29sZG93biA9IDEwCgo7IFNwZWNpZnkgd2hpY2ggcm9sZSBjYW4gZXhlY3V0ZSBhIGNvbW1hbmQuCjsgQ2FuIGN1cnJlbnRseSBvbmx5IGJlIG9uZSByb2xlLgo7IFRoZSByb2xlIG5hbWUgbmVlZHMgdG8gYmUgdGhlIGV4YWN0IHNhbWUgYXMgaW4gZGlzY29yZChpbmNsdWRpbmcgY2FwcyBhbmQgc3BlbGxpbmcpLgpsaXN0ID0gQGV2ZXJ5b25lCnN0YXR1cyA9IEBldmVyeW9uZQpzdGFydCA9IEBldmVyeW9uZQpzdG9wID0gQGV2ZXJ5b25lCnVwZGF0ZSA9IEBldmVyeW9uZQpyZWxvYWRDb25maWcgPSBAZXZlcnlvbmUKCgpbZ2FtZV9zZXJ2ZXJzXQo7IFNwZWNpZnkgaGVyZSB3aGljaCBnYW1lIHNlcnZlcnMgdGhlIGJvdCBzaG91bGQgbWFuYWdlLgo7IEZvciBleGFtcGxlIGEgZ21vZCBzZXJ2ZXIgaXMgcmVnaXN0ZXJlZCBsaWtlIHRoaXM6CjsgZ21vZHNlcnZlciA9IC9ob21lL2dtb2RzZXJ2ZXIvZ21vZHNlcnZlcgo7IFRoZSB2YWx1ZSBvbiB0aGUgbGVmdCByZXByZXNlbnRzIHRoZSBjb3JyZXNwb25kaW5nIExpbnV4IFVzZXIKOyBhbmQgdGhlIHZhbHVlIG9uIHRoZSByaWdodCByZXByZXNlbnRzIHRoZSBwYXRoIHRvIHRoZSBzZXJ2ZXIgZmlsZS4KZ21vZHNlcnZlciA9IC9ob21lL2dtb2RzZXJ2ZXIvZ21vZHNlcnZlcgptY3NlcnZlciA9IC9ob21lL21jc2VydmVyL21jc2VydmVyCgoKW2NvbW1hbmRfYWxpYXNlc10KOyBTcGxpdCBhbGlhc2VzIHdpdGggIiwiIGxpa2UgdGhpczogaGVscCxpbmZvLD8sc2VydmVyaW5mbwpoZWxwID0gaW5mbyw/LGhwCmxpc3QgPSBscwpzdGF0dXMgPSBzdGF0LHN1CnN0YXJ0ID0gc3QKc3RvcCA9IHNwCnVwZGF0ZSA9IHVkCnJlbG9hZENvbmZpZyA9IHJjCgoKW2NvbW1hbmRfZGVzY3JpcHRpb25zXQpoZWxwID0gU2hvd3MgYWxsIENvbW1hbmRzLgpzdGFydCA9IFN0YXJ0cyBhIFNlcnZlci4gW2BzdGFydCA8c2VydmVyTmFtZT5gXQpzdG9wID0gU3RvcHMgYSBTZXJ2ZXIuIFtgc3RvcCA8c2VydmVyTmFtZT5gXQo="


class Config(object):
    def __init__(self, config_path: str):
        self._config_path = config_path
        self._config = configparser.ConfigParser()
        try:
            with open(config_path):
                self._config.read(self._config_path)
        except FileNotFoundError:
            print("Config file not found. Creating a default config file.")
            with open(config_path, "wb") as file:
                file.write(base64.b64decode(default_config))
            self._config.read(self._config_path)
        except Exception as e:
            raise e

    def reload_config(self):
        self._config.read(self._config_path)

    def get_token(self):
        return self._config["general_settings"]["bot_token"]

    def get_command_prefix(self):
        try:
            return self._config["general_settings"]["command_prefix"]
        except KeyError as e:
            self.on_key_error(e)

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

    def on_key_error(self, error):
        print(f"{error} is not defined. Check the example config.ini here https://github.com/F-He/Discord_Bot_For_LGSM#example-config")
        exit()
