from timer import startTimer
from time import time
a = "(self, message, args, cmd, seconds, type, get, timers, time, timer_index, asyncio)"
async def command_handler(self, args, cmd, message, prefix, discord, timers, timer_index):
    recipies = {
        "mash": {
            # "flavour": [water, alcohol, blackberry, raspberry, apple, creekplum, alaskan ginseng, american ginseng, peach, Hop, glass bottle]
            "blackberry": [1, 2, 2, 0, 0, 0, 0, 0, 0, 0, 5],
            "raspberry": [1, 2, 0, 2, 0, 0, 0, 0, 0, 0, 5],
            "apple": [1, 2, 0, 0, 2, 0, 0, 0, 0, 0, 5],
            "creekplum": [1, 2, 0, 0, 0, 2, 0, 0, 0, 0, 5],
            "alaskangin": [1, 2, 0, 0, 0, 0, 2, 0, 0, 0, 5],
            "americangin": [1, 2, 0, 0, 0, 0, 0, 2, 0, 0, 5],
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
            "alaskangin": [1, 2, 15, 1],
            "americangin": [1, 2, 15, 1],
            "peach": [1, 2, 15, 1],
            "moonshine": [1, 2, 10, 1],
            "blackberry90p": [1, 2, 10, 1],
            "raspberry90p": [1, 2, 10, 1],
        }
    }
    if cmd == prefix + "startmash":
        await startTimer(self, message, args, cmd, 5700, "Mash", timers, timer_index)
        return

    elif cmd == prefix + "startalcohol":
        await startTimer(self, message, args, cmd, 3000, "Alcohol", timers, timer_index)
        return

    elif cmd == prefix + "startshine":
        await startTimer(self, message, args, cmd, 5700, "Shine", timers, timer_index)
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

        elif args[0] == "shine" or args[0] == "moonshine":
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

    elif cmd == prefix + "getcost":
        # calculate the cost of a recipe
        # command breakdown:
        # %getcost <type> <flavour> <quantity>

        if len(args) < 1:
            await message.channel.send(f"Incorrect usage, get help using {cmd} -h")
            return

        elif args[0] == "-h":
            await message.channel.send(f"Usage: {cmd} <type> <flavour (unless alcohol)> <quantity> \n Example: {cmd} mash raspberry batch")
            return

        elif len(args) < 2 and args[0] != "alcohol":
            await message.channel.send("You need to specify a flavour")
            return

        elif len(args) < 3 and args[0] != "alcohol":
            await message.channel.send("You need to specify a quantity")
            return

        elif args[0] == "mash":
            pricings = [0.2, 0.32, 1, 1, 1, 1, 1, 1, 1, 1, 0.2]
            for name, values in recipies["mash"].items():
                if name == args[1]:
                    cost = 0
                    for i in range(len(pricings)):
                        if values[i] != 0:
                            cost += pricings[i] * values[i]

                    if args[2] == "batch" or "case":
                        embed = discord.Embed(
                            title=f"Cost of a {args[2]} of {name} mash", description="", colour=000000)
                        embed.add_field(
                            name="Cost", value=f"{cost}", inline=False)
                        await message.channel.send(embed=embed)
                    elif args[2] == "single":
                        embed = discord.Embed(
                            title=f"Cost of {args[2]} of {name} mash", description="", colour=000000)
                        embed.add_field(
                            name="Cost", value=f"{cost/5}", inline=False)
                        await message.channel.send(embed=embed)
                    else:
                        await message.channel.send("You need to specify a quantity (batch or single)")
                        return

                    print(cost)
                    return

        elif args[0] == "alcohol":
            if args[1] == "batch":
                embed = discord.Embed(
                    title=f"Cost of a batch of alcohol", description="", colour=000000)
                embed.add_field(
                    name="Cost", value=f"3.2", inline=False)
                await message.channel.send(embed=embed)
            elif args[1] == "single":
                embed = discord.Embed(
                    title=f"Cost of a single alcohol", description="", colour=000000)
                embed.add_field(
                    name="Cost", value=f"0.32", inline=False)
                await message.channel.send(embed=embed)

        elif args[0] == "shine" or args[0] == "moonshine":
            prices = {
                # "flavour": [water, mash (quantity), glass bottle, sugar]
                "blackberry": [0.2, 0.768, 3, 1],
                "raspberry": [0.2, 0.768, 3, 1],
                "apple": [0.2, 0.768, 3, 1],
                "creekplum": [0.2, 1.536, 3, 1],
                "alaskangin": [0.2, 1.536, 3, 1],
                "americangin": [0.2, 1.536, 3, 1],
                "peach": [0.2, 1.536, 3, 1],

                "moonshine": [0.2, 1.52, 2, 1],

                "blackberry90p": [0.2, 2.992, 2, 1],
                "raspberry90p": [0.2, 2.992, 2, 1],

            }
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

            for name, values in prices.items():
                if name == args[1]:
                    # loop through the values and add them to the embed message if they are not 0
                    embed = discord.Embed(
                        title=f"Cost of {name} Shine", description="", colour=000000)

                    cost = 0
                    for i in range(len(values)):
                        if values[i] != 0:
                            cost += values[i]

                    if args[2] == "single" or args[2] == "unit":
                        # calculate the cost of a single unit of shine
                        # 15 in each batch
                        cost = cost / 15

                    embed.add_field(
                        name="Cost", value=f"{cost}", inline=False)
                    await message.channel.send(embed=embed)
                    return

    elif cmd == prefix + "help":
        embed = discord.Embed(
            title="Help", description="For help with any of the commands use <cmd> -h", colour=000000)
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
            name="Getcost", value="Gets the cost of a recipe", inline=False)
        embed.add_field(
            name="help", value="Shows this message", inline=False)
        await message.channel.send(embed=embed)
        return
    None