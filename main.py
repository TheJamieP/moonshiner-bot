import asyncio
from time import time
import discord
from discord.utils import get
from discord.ext import commands


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
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{prefix}help"))

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

        elif cmd == prefix + "getrecipe":
            # cmd breakdown: getrecipe <type> <flavour>
            # type: mash, alcohol, shine
            # flavours: blackberry, raspberry, apple, creekplum, alaskan ginseng, american ginseng, peach, moonshine, blackberry 90p, raspberry 90p
            recipies = {
                "mash": {
                    # "flavour": [water, alcohol, blackberry, raspberry, apple, creekplum, alaskan ginseng, american ginseng, peach, Hop, glass bottle]
                    "blackberry": [1, 2, 2, 0, 0, 0, 0, 0, 0, 0, 5],
                    "raspberry": [1, 2, 0, 2, 0, 0, 0, 0, 0, 0, 5],
                    "apple": [1, 2, 0, 0, 2, 0, 0, 0, 0, 0, 5],
                    "creekplum": [1, 2, 0, 0, 0, 2, 0, 0, 0, 0, 5],
                    "alaskan ginseng": [1, 2, 0, 0, 0, 0, 2, 0, 0, 0, 5],
                    "american ginseng": [1, 2, 0, 0, 0, 0, 0, 2, 0, 0, 5],
                    "peach": [1, 2, 0, 0, 0, 0, 0, 0, 2, 0, 5],
                    "moonshine": [1, 5, 0, 0, 0, 0, 0, 0, 0, 1, 5],
                    "blackberry90p": [1, 4, 5, 0, 0, 0, 0, 0, 0, 0, 5],
                    "raspberry90p": [1, 4, 0, 5, 0, 0, 0, 0, 0, 0, 5],
                },
                "alcohol": [1, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0],
                "shine": {
                    # "flavour": [water, mash (quantity), glass bottle, sugar]
                    "blackberry": [1, 1, 15, 1],
                    "raspberry": [1, 1, 15, 1],
                    "apple": [1, 1, 15, 1],
                    "creekplum": [1, 2, 15, 1],
                    "alaskan ginseng": [1, 2, 15, 1],
                    "american ginseng": [1, 2, 15, 1],
                    "peach": [1, 2, 15, 1],
                    "moonshine": [1, 2, 10, 1],
                    "blackberry90p": [1, 2, 10, 1],
                    "raspberry90p": [1, 2, 10, 1],
                }
            }

            try:
                args[0] = args[0]
                pass
            except IndexError:
                await message.channel.send(f"Incorrect usage, get help using {cmd} -h")
                return

            if args[0] == "-h":
                await message.channel.send(f"Usage: {cmd} <type> <flavour> (unless alcohol) \n Example: {cmd} mash raspberry")
                return
            if len(args) < 2 and args[0] != "alcohol":
                await message.channel.send("You need to specify a flavour")
                return

            if args[0] == "mash":
                if args[1] == "-h":
                    # list the available flavours
                    embed = discord.Embed(
                        title=f"Available flavours for Mash", description="", colour=000000)
                    string = ""
                    integer = 0
                    for name, values in recipies["mash"].items():
                        string += f"{name}, "

                    embed.add_field(
                        name="Flavours", value=string, inline=True)
                    await message.channel.send(embed=embed)
                    return
                for name, values in recipies["mash"].items():
                    if name == args[1]:
                        # loop through the values and add them to the embed message if they are not 0
                        embed = discord.Embed(
                            title=f"Recipe for {name} mash", description="", colour=000000)
                        ingredients = ["Water", "Alcohol", "Blackberry", "Raspberry", "Apple", "Creekplum",
                                       "Alaskan Ginseng", "American Ginseng", "Peach", "Hop", "Glass Bottle"]
                        for i in range(len(values)):
                            if values[i] != 0:
                                embed.add_field(
                                    name=f"{ingredients[i]}", value=f"{values[i]}", inline=False)
                        await message.channel.send(embed=embed)
                        return

                return

            elif args[0] == "alcohol":
                recipe = recipies["alcohol"]
                embed = discord.Embed(
                    title=f"Recipe for alcohol", description="", colour=000000)

                ingredients = ["Water", "Alcohol", "Blackberry", "Raspberry", "Apple", "Creekplum",
                               "Alaskan Ginseng", "American Ginseng", "Peach", "Hop", "Glass Bottle"]
                for i in range(len(recipe)):
                    if recipe[i] != 0:
                        embed.add_field(
                            name=ingredients[i], value=recipe[i], inline=False)

                await message.channel.send(embed=embed)

                return

            elif args[0] == "shine":
                if args[1] == "-h":
                    # list the available flavours
                    embed = discord.Embed(
                        title=f"Available flavours for shine", description="", colour=000000)
                    string = ""
                    integer = 0
                    for name, values in recipies["shine"].items():
                        string += f"{name}, "

                    embed.add_field(
                        name="Flavours", value=string, inline=True)
                    await message.channel.send(embed=embed)
                    return

                for name, values in recipies["shine"].items():
                    if name == args[1]:
                        # loop through the values and add them to the embed message if they are not 0
                        embed = discord.Embed(
                            title=f"Recipe for {name} Shine", description="", colour=000000)
                        ingredients = [
                            "Water", "Mash (quantity)", "Glass Bottle", "Sugar"]
                        for i in range(len(values)):
                            if values[i] != 0:
                                if i == 1:
                                    embed.add_field(
                                        name=f"{name} Mash", value=f"{values[i]}", inline=False)
                                else:
                                    embed.add_field(
                                        name=f"{ingredients[i]}", value=f"{values[i]}", inline=False)
                        await message.channel.send(embed=embed)
                        return

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
                name="Getrecipe", value="Gets the recipe for a given flavour", inline=False)
            embed.add_field(
                name="help", value="Shows this message", inline=False)
            await message.channel.send(embed=embed)
            return


client = MyClient()
client.run(token)
