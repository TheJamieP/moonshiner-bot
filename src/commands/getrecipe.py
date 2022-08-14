
async def gr(args, message, cmd, recipies, Embed):
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
            embed = Embed(
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
                embed = Embed(
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
        embed = Embed(
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
            embed = Embed(
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
                embed = Embed(
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
