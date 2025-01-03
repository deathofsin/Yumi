from discord.ext import commands
import discord

@commands.command()
async def ping(ctx):
    try:
        await ctx.send(f'Pong! {round(ctx.bot.latency * 1000)}ms')
    except Exception as e:
        print(e)
        await ctx.send("An error occurred while trying to execute this command.")