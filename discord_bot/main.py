import discord
from discord.ext import commands
from src.Config import Config
from src.Embeds import Embeds
from src.Server import ServerManager
import asyncio

config = Config(__file__[:-7] + "config.ini")
bot = commands.Bot(command_prefix=config.getCommandPrefix())
bot.remove_command("help")
embeds = Embeds(config)
server = ServerManager(config)


@bot.event
async def on_ready():
    print("Online")
    await bot.change_presence(activity=discord.Game(name=config.getBotStatus()))


@bot.command(aliases=config.getCommandAliasesFor("help"))
async def help(ctx):
    await ctx.send(embed=embeds.helpEmbed())


@bot.command(aliases=config.getCommandAliasesFor("list"))
@commands.guild_only()
@commands.has_role(config.getRoleForExecutingCommand("list"))
async def list(ctx):
    # TODO Add online status to servers
    serverList = config.getAllServers()
    await ctx.send(embed=embeds.serverList(serverList))


@bot.command(aliases=config.getCommandAliasesFor("status"))
@commands.guild_only()
@commands.has_role(config.getRoleForExecutingCommand("status"))
async def status(ctx, serverName):
    if config.checkIfServerSpecified(serverName):
        msg = await ctx.send("Checking server...")
        if await server.isOnline(serverName):
            await msg.edit(content="Server is online!")
        else:
            await msg.edit(content="Server is offline!")
    else:
        await ctx.send(f"The given server name(`{serverName}`) is not specified inside the `config.ini`")


@bot.command(aliases=config.getCommandAliasesFor("switch"))
@commands.guild_only()
@commands.has_role(config.getRoleForExecutingCommand("switch"))
@commands.cooldown(1, config.getSwitchServerCooldown(), commands.BucketType.default)
async def switch(ctx, serverName):
    if config.checkIfServerSpecified(serverName):
        msg = await ctx.send("Checking if another server is running and if so shutting it down.")
        await server.stopAll()
        await msg.edit(content=f"Starting {serverName}...")
        await server.start(serverName)
        await asyncio.sleep(2)
        if await server.isOnline(serverName):
            await msg.edit(content="Server is now online!")
        else:
            await msg.edit(content="Couldn't start the server")
    else:
        await ctx.send(f"The given server name(`{serverName}`) is not specified inside the `config.ini`")


@bot.command(aliases=config.getCommandAliasesFor("start"))
@commands.guild_only()
@commands.has_role(config.getRoleForExecutingCommand("start"))
@commands.cooldown(1, config.getStartServerCooldown(), commands.BucketType.default)
async def start(ctx, serverName):
    if config.checkIfServerSpecified(serverName):
        msg = await ctx.send(f"Starting {serverName}...")
        await ctx.trigger_typing()
        await server.start(serverName)
        await ctx.send(f"The server should be online. Check with `{config.getCommandPrefix()}status {serverName}`")
        await msg.delete()
    else:
        await ctx.send(f"The given server name(`{serverName}`) is not specified inside the `config.ini`")


@bot.command(aliases=config.getCommandAliasesFor("stop"))
@commands.guild_only()
@commands.has_role(config.getRoleForExecutingCommand("stop"))
@commands.cooldown(1, config.getStopServerCooldown(), commands.BucketType.default)
async def stop(ctx, serverName):
    if config.checkIfServerSpecified(serverName):
        msg = await ctx.send(f"Stopping {serverName}...")
        await ctx.trigger_typing()
        await server.stop(serverName)
        await ctx.send(f"The server should be offline. Check with `{config.getCommandPrefix()}status {serverName}`")
        await msg.delete()
    else:
        await ctx.send(f"The given server name(`{serverName}`) is not specified inside the `config.ini`")


@bot.command(aliases=config.getCommandAliasesFor("reloadConfig"))
@commands.guild_only()
@commands.has_role(config.getRoleForExecutingCommand("reloadConfig"))
async def reloadConfig(ctx):
    config.reloadConfig()
    await ctx.send("The config file as been reloaded.")


bot.run(config.getToken())
