from data.config import __EMBED_COLOUR__


async def hp(message, Embed):
    embed = Embed(
        title="Help", description="For help with any of the commands use <cmd> -h", colour=__EMBED_COLOUR__)
    embed.add_field(
        name="========~{Category}~========", value="======== Bootleggar ========", inline=False)
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
        name="========~{Category}~========", value="======== Farming ========", inline=False)
    embed.add_field(
        name="seedcost", value="Gets the cost of a seed", inline=False)
    embed.add_field(name="howtogrow",
                    value="tells you how to grow", inline=False)
    embed.add_field(
        name="========~{Category}~========", value="======== General ========", inline=False)
    embed.add_field(
        name="help", value="Shows this message", inline=False)
    await message.channel.send(embed=embed)
    return
