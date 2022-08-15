import asyncio
from time import time
import discord
from discord.utils import get
from discord.ext import commands
import json
from command_handler import command_handler

global prefix
prefix = "t!"
global timers
timers = []
global timer_index
timer_index = 0

#stop pushing the token to the repo
with open("./data/token.json") as f:
    token = json.load(f)["token"]


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
