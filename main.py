import discord
from discord.ext import commands
from modules.help import help
from modules.ping import ping
from modules.ban import ban
from modules.mute import *
from modules.unmute import *
import config

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

bot.add_command(help)
bot.add_command(ping)
bot.add_command(ban)
bot.add_command(mutevc)
bot.add_command(mute)
bot.add_command(unmutevc)
bot.add_command(unmute)

bot.run(config.TOKEN)