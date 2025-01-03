import discord
from discord.ext import commands
from discord.ext.commands import has_permissions

@commands.command()
@has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    try:
        await member.ban(reason=reason)
        await ctx.send(f'{member} has been banned.')
    except Exception as e:
        print(e)
        await ctx.send("An error occurred while trying to execute this command.")
