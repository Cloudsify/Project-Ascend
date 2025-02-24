"""
Project Ascend's Discord bot, Written and mainted by @Cloudsify

github.com/Cloudsify
"""


from discord.ext import commands
from Utils.EmbedBuilder import createEmbed
import json

class Ping(commands.Cog):
    """
    A cog containing hybrid command for pinging the bot to discord.
    """

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.hybrid_command(name="ping",description="Ping! Pong?", with_app_command=True)
    async def ping(self, ctx: commands.Context) -> None:
        data = {
            'title': str(round(self.bot.latency * 1000)) + "ms",
            'color': 0xf74545
        }

        embed = createEmbed(data)
        await ctx.send(embed=embed)

async def setup(bot: commands.Bot) -> None:
    """
    Required setup function for cogs
    """
    await bot.add_cog(Ping(bot))