from data.config import bootleggar_recipe_quantities as recipies, bootleggar_recipe_costs as pricings, __EMBED_COLOUR__
async def gc(args, message, cmd, Embed):
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
        for name, values in recipies["mash"].items():
            if name == args[1]:
                cost = 0
                for i in range(len(pricings)):
                    if values[i] != 0:
                        cost += pricings[i] * values[i]

                if args[2] == "batch" or "case":
                    embed = Embed(
                        title=f"Cost of a {args[2]} of {name} mash", description="", colour=__EMBED_COLOUR__)
                    embed.add_field(
                        name="Cost", value=f"{cost}", inline=False)
                    await message.channel.send(embed=embed)
                elif args[2] == "single":
                    embed = Embed(
                        title=f"Cost of {args[2]} of {name} mash", description="", colour=__EMBED_COLOUR__)
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
            embed = Embed(
                title=f"Cost of a batch of alcohol", description="", colour=__EMBED_COLOUR__)
            embed.add_field(
                name="Cost", value=f"3.2", inline=False)
            await message.channel.send(embed=embed)
        elif args[1] == "single":
            embed = Embed(
                title=f"Cost of a single alcohol", description="", colour=__EMBED_COLOUR__)
            embed.add_field(
                name="Cost", value=f"0.32", inline=False)
            await message.channel.send(embed=embed)

    elif args[0] == "shine" or args[0] == "moonshine":
        
        if args[1] == "-h":
            # list the available flavours
            embed = Embed(
                title=f"Available flavours for shine", description="", colour=__EMBED_COLOUR__)
            string = ""
            integer = 0
            for name, values in recipies["shine"].items():
                string += f"{name}, "

            embed.add_field(
                name="Flavours", value=string, inline=True)
            await message.channel.send(embed=embed)
            return

        for name, values in pricings["shine"].items():
            if name == args[1]:
                # loop through the values and add them to the embed message if they are not 0
                embed = Embed(
                    title=f"Cost of {name} Shine", description="", colour=__EMBED_COLOUR__)

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
