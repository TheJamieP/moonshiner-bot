import discord
from command_handler import command_handler
from data.config import __prefix__ as prefix, __BOT_MODE__
from os import environ
timers = []
timer_index = 0

# stop pushing the token to the repo
# load the data from the file
if __BOT_MODE__ == "dev":
    # load environment variables
    token = environ.get('DEV_TOKEN')
else:
    token = environ.get('LIVE_TOKEN')


class MyClient(discord.Client):
    async def on_ready(self):
        print("Logged on as", self.user)
        await self.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.watching, name=f"{prefix}help"
            )
        )

    async def on_message(self, message):
        if message.author.bot:
            return
        args = message.content.lower().split()
        try:
            cmd = args[0]
            args.pop(0)
        except IndexError:
            return

        await command_handler(args, cmd, message, prefix, discord, timers, timer_index, self)


client = MyClient()
client.run(token)
