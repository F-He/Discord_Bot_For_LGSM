from subprocess import Popen, PIPE
from src.Config import Config
# sudo -u gmodserver /home/gmodserver/gmodserver details


class ServerManager():
    def __init__(self, configObject: Config):
        self._config = configObject

    async def start(self, serverName):
        if self._config.serverExists(serverName):
            output = Popen(["sudo", "-u", serverName,
                            self._config.getServerFilePath(serverName), "start"], stdout=PIPE)
            return self.formatStatusLine(output)

    async def stop(self, serverName):
        if self._config.serverExists(serverName):
            output = Popen(["sudo", "-u", serverName,
                            self._config.getServerFilePath(serverName), "stop"], stdout=PIPE)
            return self.formatStatusLine(output)

    async def isOnline(self, serverName):
        if self._config.serverExists(serverName):
            output = Popen(["sudo", "-u", serverName,
                            self._config.getServerFilePath(serverName), "details"], stdout=PIPE)
            output_lines = output.stdout.readlines()
            status_line = output_lines[len(output_lines) - 2].decode("utf-8")
            if "online" in status_line.lower():
                return True
            else:
                return False
        return False

    async def stopAll(self):
        for server, serverPath in self._config.getAllServers().items():
            Popen(["sudo", "-u", server, serverPath, "stop"], stdout=PIPE)

    async def formatStatusLine(self, output):
        output_lines = output.stdout.readlines()
        status_line = output_lines[len(output_lines) - 1].decode("utf-8")
        return status_line[4:]
