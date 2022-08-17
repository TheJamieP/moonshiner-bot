from data.config import __EMBED_COLOUR__, bootleggar_recipe_costs as prices
async def sc(message, args, cmd, Embed):
        
    # cmd breakdown: {prefix}seedcost <plant>
    
    if len(args) == 0:
        embed = Embed(
            title="Error", description=f"Please provide a plant name, for a list of plants use {cmd} list", colour=__EMBED_COLOUR__)
        await message.channel.send(embed=embed)
        return
    elif args[0] == "list":
        embed = Embed(
            title="Plant List", description="", colour=__EMBED_COLOUR__)
        string = ""
        for plant in prices:
            string += plant + "\n"
        embed.add_field(name="Here is a list of all the plants", value=string)
        await message.channel.send(embed=embed)
        return 
    elif args[0] not in prices:
        embed = Embed(
            title="Error", description=f"Please provide a valid plant name, for a list of plants use {cmd} list", colour=__EMBED_COLOUR__)
        await message.channel.send(embed=embed)
        return
    plant = args[0]
    for name, price in prices.items():
        if name == plant:
            embed = Embed(
                title=f"Cost for {plant} seeds", description="", colour=__EMBED_COLOUR__)
            embed.add_field(
                name=f"For 1 {plant} seed:", value=f"{price}", inline=False)
            embed.add_field(
                name=f"For a whole plant of {plant}:", value=f"{price*2}", inline=False)
            await message.channel.send(embed=embed)
            return
    return