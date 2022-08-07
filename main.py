import asyncio
from time import time

import discord
from discord.utils import get

global prefix
prefix = "%"
global timers
timers = []
global timer_index
timer_index = 0
token = ""


class MyClient(discord.Client):

    async def on_ready(self):
        print('Logged on as', self.user)

    async def timer(self, message, args, cmd, seconds, type):
        try:
            args[0] = args[0]
            pass
        except IndexError:
            await message.channel.send(f"You need to specify a still or ask for help using {cmd} -h")
            return

        if args[0] == "-h":
            await message.channel.send(f"Usage: {cmd} <stillname> \n Example: {cmd} A")
            return
        if len(args) < 1:
            await message.channel.send("You need to specify a Still")
            return
        # ping the user after the time has passed
        role = get(message.guild.roles, name="bootleggars")
        timers.insert(timer_index, [args[0], time(
        ) + seconds, message.author.name, type])
        await message.reply(f"The {type} in still {args[0]} will be ready in {seconds} seconds")
        await asyncio.sleep(seconds)

        for timer in timers:
            time_left = int(timer[1] - time())
            if time_left <= 0:
                timers.remove(timer)
                break

        await message.channel.send(f"{role.mention} still {args[0]} is ready for another batch \n https://tenor.com/view/deliverance-movie-dance-celebrate-fun-gif-5673810")

    async def on_message(self, message):
        if message.author.bot:
            return

        args = message.content.split()
        try:
            cmd = args[0]
            args.pop(0)
        except IndexError:
            return

        if cmd == prefix + "startmash":
            await self.timer(message, args, cmd, 5700, "Mash")
            return

        elif cmd == prefix + "startalcohol":
            await self.timer(message, args, cmd, 3000, "Alcohol")
            return

        elif cmd == prefix + "startshine":
            await self.timer(message, args, cmd, 5700, "Shine")
            return

        elif cmd == prefix + "checktimers":
            embed = discord.Embed(
                title="Timers", description="", colour=000000)
            if timers != []:
                for timer in timers:
                    # structure of timer: [still, time, userid, type]
                    still = timer[0]
                    time_left = int(timer[1] - time())
                    user = timer[2]
                    type = timer[3]
                    embed.add_field(
                        name=f"Still: {still} - {type} - Started by {user}", value=f"Time Left: {time_left}", inline=False)

            else:
                embed.add_field(
                    name="No timers", value="There are no timers currently active", inline=False)

            await message.channel.send(embed=embed)
            return

        elif cmd == prefix + "help":
            embed = discord.Embed(
                title="Help", description="", colour=000000)
            embed.add_field(
                name="startmash", value="Starts a mash timer", inline=False)
            embed.add_field(
                name="startalcohol", value="Starts a alcohol timer", inline=False)
            embed.add_field(
                name="startshine", value="Starts a shine timer", inline=False)
            embed.add_field(
                name="checktimers", value="Checks the timers", inline=False)
            embed.add_field(
                name="help", value="Shows this message", inline=False)
            await message.channel.send(embed=embed)
            return


client = MyClient()


client.run(token)
