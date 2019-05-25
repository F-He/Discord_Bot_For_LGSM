from subprocess import Popen, PIPE
from src.Config import Config
import os


class ServerManager():
    def __init__(self, config_object: Config, project_path: str):
        self._config = config_object
        self._project_path = project_path

    async def start(self, server_name):
        if self._config.server_exists(server_name):
            Popen(["cd", os.path.dirname(os.path.abspath(self._config.get_server_file_path(server_name)))], stdout=PIPE)
            output = Popen(["sudo", "-u", server_name,
                            self._config.get_server_file_path(server_name), "start"], stdout=PIPE)
            return await self.format_status_line(output)

    async def stop(self, server_name):
        if self._config.server_exists(server_name):
            output = Popen(["sudo", "-u", server_name,
                            self._config.get_server_file_path(server_name), "stop"], stdout=PIPE)
            return await self.format_status_line(output)

    async def is_online(self, server_name):
        if self._config.server_exists(server_name):
            output = Popen(["sudo", "bash", self._project_path + "/src/sh/isOnline", server_name], stdout=PIPE)
            output_line = output.stdout.readline()
            status_line = output_line.decode("utf-8")
            if "1" in status_line:
                return True
            return False
        return False

    async def stop_all(self):
        for server, server_path in self._config.get_all_servers().items():
            Popen(["sudo", "-u", server, server_path, "stop"], stdout=PIPE)

    async def format_status_line(self, output):
        output_lines = output.stdout.readlines()
        status_line = output_lines[len(output_lines) - 1].decode("utf-8")
        return status_line[4:]

    async def running_server_count(self):
        server_count = 0
        for server_name, server_path in self._config.get_all_servers().items():
            if await self.is_online(server_name):
                server_count += 1
        return server_count

    async def get_server_status_dict(self):
        server_dict = {}
        for server_name in self._config.get_all_servers():
            is_server_online = await self.is_online(server_name)
            if is_server_online:
                server_dict[server_name] = "`✔️ Online`"
            else:
                server_dict[server_name] = "`❌ Offline`"
        return server_dict
