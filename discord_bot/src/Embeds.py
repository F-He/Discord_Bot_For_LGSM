import discord
from src.Config import Config
from src.Server import ServerManager


class Embeds():
    def __init__(self, configObject: Config):
        self._config = configObject

    def helpEmbed(self):
        embed = self.defaultEmbed("Help", f"You can use all those commands with the `{self._config.getCommandPrefix()}` prefix.")
        self.addHelpEmbedFields(embed)
        return embed

    def addHelpEmbedFields(self, embed: discord.Embed):
        for command, desc in self._config.getCommandsWithDescription().items():
            embed.add_field(name=f"`{command}`", value=desc, inline=False)

    async def serverList(self, serverObject: ServerManager):
        serverDict = await serverObject.getServerStatusDict()
        embed = self.defaultEmbed("Server List", await self.serverListDescription(serverDict))
        return embed

    async def serverListDescription(self, serverDict: dict):
        description = "==============\n"
        for serverName, status in serverDict.items():
            description += f"{serverName}: {status}\n"
            description += "==============\n"
        return description

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
