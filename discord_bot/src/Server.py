from subprocess import Popen, PIPE
from src.Config import Config
# sudo -u gmodserver /home/gmodserver/gmodserver details
# tmux list-sessions -F "mcserver" 2>/dev/null | grep -Ecx "mcserver"
# tmux list-sessions -F "mcserver" 2>/dev/null | grep -Ecx "mcserver"


class ServerManager():
    def __init__(self, configObject: Config):
        self._config = configObject

    async def start(self, serverName):
        if self._config.serverExists(serverName):
            output = Popen(["sudo", "-u", serverName,
                            self._config.getServerFilePath(serverName), "start"], stdout=PIPE)
            return await self.formatStatusLine(output)

    async def stop(self, serverName):
        if self._config.serverExists(serverName):
            output = Popen(["sudo", "-u", serverName,
                            self._config.getServerFilePath(serverName), "stop"], stdout=PIPE)
            return await self.formatStatusLine(output)

    async def isOnline(self, serverName):
        if self._config.serverExists(serverName):
            output = Popen(["sudo", "bash", "/home/finn/discord-bots/Discord_Bot_For_LGSM/discord_bot/src/sh/isOnline", serverName], stdout=PIPE)
            output_line = output.stdout.readline()
            status_line = output_line.decode("utf-8")
            print(status_line[0])
            if "1" in status_line:
                return True
            return False
        return False

    async def stopAll(self):
        for server, serverPath in self._config.getAllServers().items():
            Popen(["sudo", "-u", server, serverPath, "stop"], stdout=PIPE)

    async def formatStatusLine(self, output):
        output_lines = output.stdout.readlines()
        status_line = output_lines[len(output_lines) - 1].decode("utf-8")
        return status_line[4:]
