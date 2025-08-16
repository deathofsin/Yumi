import discord
from discord.ext import commands


@commands.command()
async def help(ctx):
    try:
        embed = discord.Embed(title="Yumi Commands", 
                            description="""
                            ✦ !help - Shows all the commands
                            ✦ !ping - Shows the bot's latency
                            ✦ !ban - Bans a member
                            ✦ !unban - Unbans a member
                            ✦ !mutevc - Mutes a member in a voice channel
                            ✦ !mute - Mutes a member
                            ✦ !unmutevc - Unmutes a member in a voice channel
                            ✦ !unmute - Unmutes a member
                            ✦ !kick - Kicks a member
                            """, 
                            color=discord.Color.dark_purple())
        embed.set_author(name="Yumi")
        embed.add_field(name="Github", value="[Lain Github](https://github.com/deathofsin)")
        embed.add_field(name="Invite", value="[Invite Yumi in your server](https://discord.com/oauth2/authorize?client_id=1323313408652869643&permissions=8&integration_type=0&scope=bot)")
        await ctx.send(embed=embed)
    except Exception as e:
        print(e)
        await ctx.send("An error occurred while trying to execute this command.")

