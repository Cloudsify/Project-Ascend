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
        """
        First function that the library runs before anything else.
        TODO: Call load_cogs from here and any other essentials.
        :return:
        """

        print("---------------------------")
        Logger.info(f"Logged in as {self.user}!")
        Logger.info(f"Python Version: {platform.python_version()}")
        Logger.info(f"Platform: {platform.system()} {platform.release()} ({os.name})")
        Logger.info(f"Discord API version: {discord.__version__}")
        print("---------------------------")

        await self.load_cogs()

    async def load_cogs(self) -> None:
        """
        Loads the commands from other files in the cogs folder or subdirectories
        """

        extensions_found = False

        for root, dirs, files in os.walk(f"{os.path.realpath(os.path.dirname(__file__))}/cogs"):
            for file in files:
                if file.endswith(".py"):
                    extensions_found = True
                    extension = os.path.splitext(file)[0]
                    try:
                        module_path = os.path.relpath(root, os.path.realpath(os.path.dirname(__file__)) + '/cogs')
                        if module_path == ".":
                            module_path = ""
                        full_extension = f"cogs.{module_path.replace(os.sep, '.')}.{extension}" if module_path else f"cogs.{extension}"

                        await self.load_extension(full_extension)
                        Logger.info(f"Loaded extension '{full_extension}'")
                    except Exception as e:
                        exception = f"{type(e).__name__}: {e}"
                        Logger.error(f"Failed to load extension {full_extension}\n{exception}")

        if not extensions_found:
            Logger.warning("No cogs were found.. The bot won't do much without them!")

bot = Bot()
bot.run(config['token'])