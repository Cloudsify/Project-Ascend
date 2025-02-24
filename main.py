"""
Project Ascend's Discord bot, Written and mainted by @Cloudsify

github.com/Cloudsify
"""
import discord, os, platform, sys, json
from discord.ext import commands, tasks

"""
Our custom imports, Utils and any other things we need
"""
from Utils import Logger

if not os.path.isfile(f"{os.path.realpath(os.path.dirname(__file__))}/config.json"):
    sys.exit("'config.json' not found! Please add it and try again.")
else:
    with open(f"{os.path.realpath(os.path.dirname(__file__))}/config.json") as file:
        config = json.load(file)

intents = discord.Intents.all()


class Bot(commands.Bot):
    def __init__(self) -> None:
        super().__init__(
            command_prefix=":::::::::::::::::::::NULL", # Set this to a random string. Less chance of someone executing it!
            intents=intents,
            help_command=None,
        )

    async def on_ready(self):
        print("---------------------------")
        Logger.info(f"Logged in as {self.user}!")
        Logger.info(f"Python Version: {platform.python_version()}")
        Logger.info(f"Platform: {platform.system()} {platform.release()} ({os.name})")
        Logger.info(f"Discord API version: {discord.__version__}")
        print("---------------------------")

    async def load_cogs(self) -> None:
        """
        Loads the commands from other files in the cogs folder
        """
        for file in os.listdir(f"{os.path.realpath(os.path.dirname(__file__))}/cogs"):
            if file.endswith(".py"):
                extension = file[:-3]
                try:
                    await self.load_extension(f"cogs.{extension}")
                    Logger.info(f"Loaded extension '{extension}'")
                except Exception as e:
                    exception = f"{type(e).__name__}: {e}"
                    Logger.error(
                        f"Failed to load extension {extension}\n{exception}"
                    )

bot = Bot()
bot.run(config['token'])