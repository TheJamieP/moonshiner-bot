async def hp(message, Embed):
    embed = Embed(
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
