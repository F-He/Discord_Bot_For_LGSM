import discord
from src.Config import Config


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

    def serverList(self, serverList: list):
        embedDescription = ""
        for server in serverList:
            embedDescription += f"{server}\n"
        embed = discord.Embed(
            title="Server List",
            description=embedDescription,
            colour=self._config.getBotEmbedColor()
        )
        return embed
