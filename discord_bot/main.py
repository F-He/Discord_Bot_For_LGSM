import discord
from discord.ext import commands
from src.Config import Config

config = Config(__file__[:-7] + "config.ini")
bot = commands.Bot(command_prefix=config.get_command_prefix())
bot.remove_command("help")

@bot.event
async def on_ready():
    print("Online")
    await bot.change_presence(activity=discord.Game(name=config.get_bot_status()))


@bot.command(aliases=config.get_command_aliases_for("help"))
async def help(ctx):
    pass

bot.run(config.get_token())
