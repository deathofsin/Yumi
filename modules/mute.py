import discord
from discord.ext import commands


@commands.command()
async def mutevc(ctx, member: discord.Member, *, reason=None):
    try:
        await member.edit(mute=True, reason=reason)
        await ctx.send(f'{member} has been muted.')
    except Exception as e:
        print(e)
        await ctx.send("An error occurred while trying to execute this command.")

@commands.command()
async def mute(ctx, member: discord.Member, *, reason=None):
    try:
        muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
        if not muted_role:
            muted_role = await ctx.guild.create_role(name="Muted")

            for channel in ctx.guild.channels:
                await channel.set_permissions(muted_role, speak=False, send_messages=False, read_message_history=True, read_messages=False)

        await member.add_roles(muted_role, reason=reason)
        await ctx.send(f'{member} has been muted.')
    except Exception as e:
        print(e)
        await ctx.send("An error occurred while trying to execute this command.")