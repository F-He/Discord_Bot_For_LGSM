import discord
from src.Config import Config


class Embeds():
    def __init__(self, configObject: Config):
        self._config = configObject

    def helpEmbed(self):
        embed = discord.Embed(
            title="Help",
            description=f"You can use all those commands with the `{self._config.get_command_prefix()}` prefix.",
            colour=self._config.get_bot_embed_color()
            )
        for command, desc in self._config.get_commands_with_description().items():
            embed.add_field(
                name=command,
                value=desc,
                inline=False
            )
        return embed