import discord
from discord.ext import commands


@commands.command()
async def unmutevc(ctx, member: discord.Member):
    try:
        await member.edit(mute=False)
        await ctx.send(f'{member} has been unmuted.')
    except Exception as e:
        print(e)
        await ctx.send("An error occurred while trying to execute this command.")


@commands.command()
async def unmute(ctx, member: discord.Member):
    try:
        muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
        if muted_role in member.roles:
            await member.remove_roles(muted_role)
            await ctx.send(f'{member} has been unmuted.')
        else:
            await ctx.send(f'{member} is not muted.')
    except Exception as e:
        print(e)
        await ctx.send("An error occurred while trying to execute this command.")