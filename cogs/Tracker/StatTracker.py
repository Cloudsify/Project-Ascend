"""
Project Ascend's Discord bot, Written and mainted by @Cloudsify

github.com/Cloudsify
"""

import discord
from discord import app_commands
from discord.ext import commands
from Utils.EmbedBuilder import createEmbed

class StatTracker(commands.Cog):
    """
    A cog containing a hybrid command for displaying rank information.
    """

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.hybrid_command(name="rank", description="Displays rank info for selected game")
    @app_commands.choices(game=[
        app_commands.Choice(name="Rocket League", value="rocketleague"),
        app_commands.Choice(name="VALORANT", value="valorant"),
    ])
    async def rank(self, ctx: commands.Context, game: app_commands.Choice[str], username: str) -> None:
        """
        A hybrid command that shows the rank for a selected game (Rocket League or Valorant).
        """
        if game.value == 'rocketleague':
            GameTitle = "Rocket League"
        elif game.value == 'valorant':
            GameTitle = "VALORANT"


        data = {
            'title': f"{game.value} Rank Information",
            'description': f"Your rank in {game.value} is: {rank}",
            'color': 0xf74545
        }

        # Create the embed
        embed = createEmbed(data)

        # Send the embed
        await ctx.send(embed=embed)


async def setup(bot: commands.Bot) -> None:
    """
    Required setup function for cogs

    Disabled till I can find a better API for Rocket League and VALORANT
    """
    #await bot.add_cog(StatTracker(bot))  # Corrected from Ping to StatTracker
