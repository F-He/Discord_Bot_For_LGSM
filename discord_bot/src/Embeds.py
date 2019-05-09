import discord
from src.Config import Config
from src.Server import ServerManager


class Embeds():
    def __init__(self, configObject: Config):
        self._config = configObject

    def helpEmbed(self):
        embed = discord.Embed(
            title="Help",
            description=f"You can use all those commands with the `{self._config.getCommandPrefix()}` prefix.",
            colour=self._config.getBotEmbedColor()
        )
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
                serverDict[serverName] = "Online"
            else:
                serverDict[serverName] = "Offline"

        embedDescription = ""
        for serverName, status in serverList.items():
            embedDescription += f"{serverName}: {status}\n"
        embed = discord.Embed(
            title="Server List",
            description=embedDescription,
            colour=self._config.getBotEmbedColor()
        )
        return embed
