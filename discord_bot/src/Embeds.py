import discord
from src.Config import Config
from src.Server import ServerManager


class Embeds():
    def __init__(self, configObject: Config):
        self._config = configObject

    def help_embed(self):
        embed = self.default_embed("Help", f"You can use all those commands with the `{self._config.get_command_prefix()}` prefix.")
        self.add_help_embed_fields(embed)
        return embed

    def add_help_embed_fields(self, embed: discord.Embed):
        for command, desc in self._config.get_commands_with_description().items():
            embed.add_field(name=f"`{command}`", value=desc, inline=False)

    async def server_list(self, server_object: ServerManager):
        server_dict = await server_object.get_server_status_dict()
        embed = self.default_embed("Server List", await self.server_list_description(server_dict))
        return embed

    async def server_list_description(self, server_dict: dict):
        description = "==============\n"
        for server_name, status in server_dict.items():
            description += f"{server_name}: {status}\n"
            description += "==============\n"
        return description

    async def max_parallel_server_count_exceeded(self):
        embed = self.default_embed(
            "Max parallel server count exceeded!",
            f"Stop another Server with `{self._config.get_command_prefix()}stop serverName` or increase the `max_parallel_running_count` setting inside the `config.ini` file."
        )
        return embed

    async def is_online(self):
        embed = self.default_embed("Server Status", "✔️ Is Online", 0x1cd10c)
        return embed

    async def is_offline(self):
        embed = self.default_embed("Server Status", "❌ Is Offline", 0xce0808)
        return embed

    def default_embed(self, title, description, color=None):
        embed_color = color
        if color is None:
            embed_color = self._config.get_bot_embed_color()
        default_embed = discord.Embed(
            title=title,
            description=description,
            colour=embed_color
        )
        return default_embed
