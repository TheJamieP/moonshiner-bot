from data.config import __EMBED_COLOUR__


async def gd(message, Embed, client):
    # wait for a reaction to move the arrow to the next page
    await message.add_reaction("⬅") or await message.add_reaction("➡")
    embed = Embed(
        title="Fishing Guide", description="For help with anything fishing related!", footer="fishing", colour=__EMBED_COLOUR__)
    embed.add_field(
        name="========~{Category}~========", value="======== Bait ========", inline=False)
    embed.add_field(
        name="Cheese", value="Used everywhere. Best for catching bluegill or rock bass", inline=False)
    embed.add_field(
        name="Bread", value="Used everywhere. Best for catching smaller perch  redfin and pickerel ", inline=False)
    embed.add_field(
        name="Corn", value="Used everywhere Best for catching smaller catfish and chain pickerel", inline=False)
    embed.add_field(
        name="Live Worms", value="Used in Lakes. Great for catching Steelhead trout", inline=False)
    embed.add_field(
        name="Crickets", value="Used in rivers. Great for catching small mouth bass", inline=False)
    embed.add_field(
        name="Crayfish", value="Used in swamps. Great for largemouth bass", inline=False)
    embed.add_field(
        name="========~{Category}~========", value="======== Lures ========", inline=False)
    embed.add_field(
        name="Lake Lure", value="Used in lakes. Great for sturgeon and muskie ", inline=False)
    embed.add_field(
        name="River Lure", value="Used in rivers. Good For catching nothern pike and sockeye salmon", inline=False)
    embed.add_field(
        name="Swamp Lure", value="Used in Lakes. Good or catching channel cats and longnose gar", inline=False)

    await message.channel.send(embed=embed)
    return
