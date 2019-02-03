import discord
from discord.ext import commands
from src.Config import Config
from src.Embeds import Embeds

config = Config(__file__[:-7] + "config.ini")
bot = commands.Bot(command_prefix=config.get_command_prefix())
bot.remove_command("help")
embeds = Embeds(config)

@bot.event
async def on_ready():
    print("Online")
    await bot.change_presence(activity=discord.Game(name=config.get_bot_status()))


@bot.command(aliases=config.get_command_aliases_for("help"))
async def help(ctx):
    await ctx.send(embed=embeds.helpEmbed())


@bot.command(aliases=config.get_command_aliases_for("switch"))
@commands.guild_only()
@commands.cooldown(1, config.get_switch_server_cooldown(), commands.BucketType.default)
async def switch(ctx, server_name):
    await ctx.send("Check if another server is running and if so, shutting it down.")
    # Check and stop servers
    await ctx.send(f"Starting {server_name} server.")
    # Start server


bot.run(config.get_token())
