
async def sc(message, args, cmd, Embed):
    prices = {
        #name : price
        "indiantobacco": 0.35,
        "coffee": 0.2,
        "alaskanginseng": 0.15,
        "americanginseng": 0.15,
        "hop": 0.25,
        "blackberry": 0.2,
        "blackcurrant": 0.15,
        "bloodflower": 0.25,
        "chocdaisy": 0.2,
        "creekplum": 0.2,
        "creekingthyme": 0.2,
        "crowsgarlic": 0.2,
        "englishmace": 0.2,
        "milksage": 0.25,
        "oleandersage": 0.15,
        "oregano": 0.4,
        "parasolmushroom": 0.4,
        "priarepoppy": 0.5,
        "redraspberry": 0.25,
        "redsage": 0.2,
        "tea": 0.27,
        "wildcarrot": 0.15,
        "wildmint": 0.25,
        "wintergreenberry": 0.3,
        "yarrow": 0.25,
        "corn": 0.25,
        "apple": 0.3,
        "sugarcane": 0.2,
        "potato": 0.1,
        "cocoa": 0.35,
        "peach": 0.25,

    }
    # cmd breakdown: {prefix}seedcost <plant>
    
    if len(args) == 0:
        embed = Embed(
            title="Error", description=f"Please provide a plant name, for a list of plants use {cmd} list", colour=000000)
        await message.channel.send(embed=embed)
        return
    elif args[0] == "list":
        embed = Embed(
            title="Plant List", description="", colour=000000)
        string = ""
        for plant in prices:
            string += plant + "\n"
        embed.add_field(name="Here is a list of all the plants", value=string)
        await message.channel.send(embed=embed)
        return 
    elif args[0] not in prices:
        embed = Embed(
            title="Error", description=f"Please provide a valid plant name, for a list of plants use {cmd} list", colour=000000)
        await message.channel.send(embed=embed)
        return
    plant = args[0]
    for name, price in prices.items():
        if name == plant:
            embed = Embed(
                title=f"Cost for {plant} seeds", description="", colour=000000)
            embed.add_field(
                name=f"For 1 {plant} seed:", value=f"{price}", inline=False)
            embed.add_field(
                name=f"For a whole plant of {plant}:", value=f"{price*2}", inline=False)
            await message.channel.send(embed=embed)
            return
    return