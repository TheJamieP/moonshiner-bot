import pymongo
from data.config import __EMBED_COLOUR__, __prefix__
from data.sensitive import get_connection_string


database = pymongo.MongoClient(
    get_connection_string()).get_database("moonshiner")


async def fetchData():
    column = database.orders
    data = column.find({})
    data = [x for x in data]
    return column, data


async def add_order(message, flavour, quantity, customer):
    column, data = await fetchData()
    if data == []:
        id = 1
    else:
        id = data[len(data) - 1]["id"] + 1
    column.insert_one(
        {
            "user": message.author.name,
            "flavour": flavour,
            "quantity": quantity,
            "customer": customer,
            "id": id
        }
    )
    pass


async def remove_order(message, id):
    column = database.orders
    column.delete_one(
        {
            "id": id
        }
    )
    pass


async def get_orders(message, Embed):
    column, data = await fetchData()
    if data == []:
        await message.channel.send(
            embed=Embed(
                title="Orders",
                description="There are no orders.",
                color=__EMBED_COLOUR__,
            )
        )
        return
    embed = Embed(
        title=f"Orders", description=f"", color=__EMBED_COLOUR__)
    for d in data:
        for name, value in d.items():
            if name == "user":
                user = value
            elif name == "flavour":
                flavour = value
            elif name == "quantity":
                quantity = value
            elif name == "customer":
                customer = value
            elif name == "id":
                id = value

        embed.add_field(
            name=f"Order for:  {customer}", value=f"Flavour:  {flavour},\n Quantity(Bottles):  {quantity},\n  Message Creator:  {user},\n Order ID:  {id}", inline=True)

        pass

    await message.channel.send(embed=embed)


async def order(message, args, cmd, Embed):
    # cmd breakdown:
    # order <add> <flavour> <quantity> <customer>
    # order <remove> <id>
    # order <get>
    try:
        param = args[0]

    except IndexError:
        await message.channel.send(
            embed=Embed(
                title="Error - No Parameter",
                description="Please enter a valid parameter. (add/remove/get)",
                color=__EMBED_COLOUR__,
            )
        )
        return

    if param == "add":
        if args[1] == "-h":
            await message.channel.send(
                embed=Embed(
                    title="Help",
                    description=f"{__prefix__}order add <flavour> <quantity> <customer>",
                    color=__EMBED_COLOUR__,
                )
            )
            return
        flavour = args[1]
        quantity = int(args[2])
        customer = args[3]
        await add_order(message, flavour, quantity, customer)

    elif param == "remove":
        if args[1] == "-h":
            await message.channel.send(
                embed=Embed(
                    title="Help",
                    description=f"{__prefix__}order remove <id>",
                    color=__EMBED_COLOUR__,
                )
            )
            return
        id = int(args[1])
        await remove_order(message, id)

    elif param == "get":
        try:
            if args[1] == "-h":
                await message.channel.send(
                    embed=Embed(
                        title="Help",
                        description=f"{__prefix__}order get - Gets all orders.",
                        color=__EMBED_COLOUR__,
                    )
                )
            return
        except IndexError:
            print("no args")
            await get_orders(message, Embed)
            return
    else:
        await message.channel.send(
            embed=Embed(
                title="Error - Invalid Parameter",
                description="Please enter a valid parameter. (add/remove/get)",
                color=__EMBED_COLOUR__,
            )
        )
