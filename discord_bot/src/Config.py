import configparser
from src.Utils import convert_str_to_hex


class Config(object):
    def __init__(self, configPath: str):
        self._configPath = configPath
        self._config = configparser.ConfigParser()
        self._config.read(self._configPath)

    def reloadConfig(self):
        self._config.read(self._configPath)

    def getToken(self):
        return self._config["general_settings"]["bot_token"]

    def getCommandPrefix(self):
        return self._config["general_settings"]["command_prefix"]

    def getBotStatus(self):
        return self._config["general_settings"]["bot_status"]

    def getCommandAliasesFor(self, command_name: str):
        return str(self._config["command_aliases"][command_name]).split(",")

    def getBotEmbedColor(self):
        return convert_str_to_hex(self._config["general_settings"]["bot_embed_color"])

    def getCommandsWithDescription(self):
        return self._config._sections["command_descriptions"]

    def getSwitchServerCooldown(self):
        return self._config["command_settings"]["switch_server_cooldown"]

    def getStartServerCooldown(self):
        return self._config["command_settings"]["start_server_cooldown"]

    def getStopServerCooldown(self):
        return self._config["command_settings"]["stop_server_cooldown"]

    def serverExists(self, serverName):
        if serverName not in self._config["game_servers"]:
            return False
        else:
            return True

    def getServerFilePath(self, serverName):
        return self._config["game_servers"][serverName]

    def getAllServers(self):
        return self._config["game_servers"]

    def getRoleForExecutingCommand(self, commandName):
        return self._config["command_settings"][commandName]

    def checkIfServerSpecified(self, serverName):
        return self._config.has_option("game_servers", serverName)
