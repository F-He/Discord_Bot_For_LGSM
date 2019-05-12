import discord
from src.Config import Config
from src.Server import ServerManager


class Embeds():
    def __init__(self, configObject: Config):
        self._config = configObject

    def helpEmbed(self):
        embed = self.defaultEmbed("Help", f"You can use all those commands with the `{self._config.getCommandPrefix()}` prefix.")
        for command, desc in self._config.getCommandsWithDescription().items():
            embed.add_field(
                name=f"`{command}`",
                value=desc,
                inline=False
            )
        return embed

    async def serverList(self, serverObject: ServerManager):
        serverList = self._config.getAllServers()
        serverDict = {}
        for serverName in serverList:
            isServerOnline = await serverObject.isOnline(serverName)
            if isServerOnline:
                serverDict[serverName] = "`✔️ Online`"
            else:
                serverDict[serverName] = "`❌ Offline`"

        embedDescription = "==============\n"
        for serverName, status in serverDict.items():
            embedDescription += f"{serverName}: {status}\n"
            embedDescription += "==============\n"
        embed = self.defaultEmbed("Server List", embedDescription)
        return embed

    async def maxParallelServerCountExceeded(self):
        embed = self.defaultEmbed(
            "Max parallel server count exceeded!",
            f"Stop another Server with `{self._config.getCommandPrefix()}stop serverName` or increase the `max_parallel_running_count` setting inside the `config.ini` file."
        )
        return embed

    async def isOnline(self):
        embed = self.defaultEmbed("Server Status", "✔️ Is Online", 0x1cd10c)
        return embed

    async def isOffline(self):
        embed = self.defaultEmbed("Server Status", "❌ Is Offline", 0xce0808)
        return embed

    def defaultEmbed(self, title, description, color=None):
        embedColor = color
        if color is None:
            embedColor = self._config.getBotEmbedColor()
        defaultEmbed = discord.Embed(
            title=title,
            description=description,
            colour=embedColor
        )
        return defaultEmbed
