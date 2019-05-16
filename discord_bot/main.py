import discord
import os
from discord.ext import commands
from src.Config import Config
from src.Embeds import Embeds
from src.Server import ServerManager
from src.Updater import Updater

project_path = os.path.dirname(os.path.abspath(__file__))
updater = Updater(project_path)
__version__ = updater.get_version()

updater.start()

config = Config(project_path + "/config.ini")
bot = commands.Bot(command_prefix=config.get_command_prefix())
bot.remove_command("help")
embeds = Embeds(config)
server = ServerManager(config, project_path)


@bot.event
async def on_ready():
    startup_prints()
    await bot.change_presence(activity=discord.Game(name=config.get_bot_status()))


@bot.command(aliases=config.get_command_aliases_for("help"))
async def help(ctx):
    await ctx.send(embed=embeds.help_embed())


@bot.command(aliases=config.get_command_aliases_for("list"))
@commands.guild_only()
@commands.has_role(config.get_role_for_executing_command("list"))
async def list(ctx):
    await ctx.send(embed=await embeds.server_list(server))


@bot.command(aliases=config.get_command_aliases_for("status"))
@commands.guild_only()
@commands.has_role(config.get_role_for_executing_command("status"))
async def status(ctx, server_name):
    if config.check_if_server_specified(server_name):
        msg = await ctx.send("Checking server...")
        if await server.is_online(server_name):
            await msg.edit(embed=await embeds.is_online())
        else:
            await msg.edit(embed=await embeds.is_offline())
    else:
        await ctx.send(f"The given server name(`{server_name}`) is not specified inside the `config.ini`")


@bot.command(aliases=config.get_command_aliases_for("start"))
@commands.guild_only()
@commands.has_role(config.get_role_for_executing_command("start"))
@commands.cooldown(1, config.get_start_server_cooldown(), commands.BucketType.default)
async def start(ctx, server_name):
    if config.check_if_server_specified(server_name):
        if await server_allowed_to_start():
            msg = await ctx.send(f"Starting {server_name}...")
            await ctx.trigger_typing()
            await server.start(server_name)
            await ctx.send(f"The server should be online. Check with `{config.get_command_prefix()}status {server_name}`")
            await msg.delete()
        else:
            await ctx.send(embed=await embeds.max_parallel_server_count_exceeded())
    else:
        await ctx.send(f"The given server name(`{server_name}`) is not specified inside the `config.ini`")


@bot.command(aliases=config.get_command_aliases_for("stop"))
@commands.guild_only()
@commands.has_role(config.get_role_for_executing_command("stop"))
@commands.cooldown(1, config.get_stop_server_cooldown(), commands.BucketType.default)
async def stop(ctx, server_name):
    if config.check_if_server_specified(server_name):
        msg = await ctx.send(f"Stopping {server_name}...")
        await ctx.trigger_typing()
        await server.stop(server_name)
        await ctx.send(f"The server should be offline. Check with `{config.get_command_prefix()}status {server_name}`")
        await msg.delete()
    else:
        await ctx.send(f"The given server name (`{server_name}`) is not specified inside the `config.ini`")


@bot.command(aliases=config.get_command_aliases_for("update"))
@commands.guild_only()
@commands.has_role(config.get_role_for_executing_command("update"))
async def update(ctx):
    await ctx.send("Starting update.")
    updater.start()


@bot.command(aliases=config.get_command_aliases_for("reloadConfig"))
@commands.guild_only()
@commands.has_role(config.get_role_for_executing_command("reloadConfig"))
async def reloadConfig(ctx):
    config.reload_config()
    await ctx.send("The config file as been reloaded.")


async def server_allowed_to_start():
    if config.is_parallel_running_allowed():
        if await server.running_server_count() < config.get_max_parallel_running_count():
            return True
        else:
            return False
    else:
        if await server.running_server_count() < 1:
            return True
        else:
            return False


def startup_prints():
    print("========Online========")
    print(f"Bot Version: {__version__}")
    print(f"Discord.py Version: {discord.__version__}")
    print(f"Latency: {round(bot.latency, 2)} sec")
    print(f"Connected as: {bot.user.name}")
    print(f"Path: {project_path}")


bot.run(config.get_token())
