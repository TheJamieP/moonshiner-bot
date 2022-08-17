import discord
from command_handler import command_handler

global prefix
prefix = "t!"
global timers
timers = []
global timer_index
timer_index = 0

# stop pushing the token to the repo
# load the data from the file
try:
    token = open("./src/data/token.txt", "r").read()
except FileNotFoundError:
    print("Token file not found")
    # create the file
    open("./src/data/token.txt", "w").close()
    # write the token to the file
    token = open("./src/data/token.txt", "w").write(input("Enter your token: "))
    token = open("./src/data/token.txt", "r").read()

class MyClient(discord.Client):

    async def on_ready(self):
        print('Logged on as', self.user)
        await self.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{prefix}help"))

    async def on_message(self, message):
        if message.author.bot:
            return
        args = message.content.split()
        try:
            cmd = args[0]
            args.pop(0)
        except IndexError:
            return

        await command_handler(args, cmd, message, prefix, discord, timers, timer_index)


client = MyClient()
client.run(token)
