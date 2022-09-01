import pymongo
from data.config import __EMBED_COLOUR__, __prefix__, __orders_channel__
from os import environ
from asyncio import TimeoutError, sleep


database = pymongo.MongoClient(
    environ.get("CONNECTION_STRING")).get_database("orders")


async def order(message, args, cmd, Embed, client):
    # cmd breakdown:
    # order <add> <business> <item> <quantity> <customer>
    # order <remove> <business> <id>
    # order <get> <business>
    try:
        param = args[0]

    except IndexError:

        await message.channel.send(
            embed=Embed(
                title="Error - No Parameter",
                description="Please enter a valid parameter. (add/remove/get)",
                footer="Message deleting in 5 seconds",
                color=__EMBED_COLOUR__,
            )
        )

        return
    if param != "add" and param != "remove" and param != "get":
        await message.channel.send(
            embed=Embed(
                title="Error - Invalid Parameter",
                description="Please enter a valid parameter. (add/remove/get)",
                footer="Message deleting in 5 seconds",
                color=__EMBED_COLOUR__,
            )
        )

        return
    try:
        role = args[1]
    except IndexError:
        await message.channel.send(
            embed=Embed(
                title="Error - No Role",
                description="Please enter a valid role. (mining, chef, farmer, fisher, hunter, lumberjack, bootlegger, blacksmith, gunsmith, horsetrainer, ranching, pharmacist)",
                footer="Message deleting in 5 seconds",
                color=__EMBED_COLOUR__,
            )
        )
        msg = await client.wait_for("message", timeout=1.0)

        return
    possible_roles = ["mining", "chef", "farmer", "fisher", "hunter", "lumberjack",
                      "bootlegger", "blacksmith", "gunsmith", "horsetrainer", "ranching", "pharmacist", "carpenter"]

    if role not in possible_roles:
        embed = Embed(
            title="Error - Invalid Role",
            description="Please enter a valid role. (mining, chef, farmer, fisher, hunter, lumberjack, bootlegger, blacksmith, gunsmith, horsetrainer, ranching, pharmacist)",
            footer="Message deleting in 5 seconds",
            color=__EMBED_COLOUR__,
        )
        await message.channel.send(embed=embed)

        return
    column = database.get_collection(role)
    if param == "add":
        if message.channel.id != __orders_channel__:
            await message.channel.send(
                embed=Embed(
                    title="Error",
                    description="This command can only be used in the orders channel.",

                    colour=__EMBED_COLOUR__
                ))

            return

        # begin taking items from a new message and adding them to the list of items
        items = {
            # "item": "quantity"
        }
        loop = True
        while loop:
            try:
                await message.channel.send("Please enter the name of the item you would like to add. (type done when finished): ")
                await sleep(0.10)
                item = await client.wait_for("message", timeout=600.0)
                # check if the item message author is the same as the message author and keep listening if they are not the same
                if item.author != message.author:
                    continue

                if item.content == "done":
                    break
                await message.channel.send("Please enter the quantity of the item you would like to add:")
                quantity = await client.wait_for("message", timeout=600.0)
                items[item.content] = quantity.content

            except TimeoutError:
                break

        await message.channel.send("Please enter the name of the customer:")
        customer = await client.wait_for("message", timeout=600.0)

        customer = customer.content.lower()
        await message.channel.send("Please enter the type of the order. (incoming/outgoing):")
        type = await client.wait_for("message", timeout=600.0)
        await message.channel.purge(limit=75)
        type = type.content.lower()
        data = [x for x in column.find({})]
        if data == []:
            id = 1
        else:
            id = data[len(data) - 1]["Id"] + 1
        column.insert_one(
            {
                "Author": message.author.name,
                "Items": items,
                "Customer": customer,
                "Type": type,
                "Id": id
            }
        )

    elif param == "get":
        orders = [x for x in column.find({})]
        if orders == []:
            await message.channel.send(
                embed=Embed(
                    title="Error - No Orders",
                    description="There are no orders in this category.",

                    color=__EMBED_COLOUR__,
                )
            )

            return
        embed = Embed(title="Orders", description="", color=__EMBED_COLOUR__)
        for order in orders:
            for fields in order:
                if fields == "Items":
                    items = ""
                    for name, quantity in order[fields].items():
                        items += f"{name}: {quantity}, "

                elif fields == "Id":
                    id = order[fields]
                elif fields == "Author":
                    author = order[fields]
                elif fields == "Customer":
                    customer = order[fields]
                elif fields == "Type":
                    type = order[fields]

            embed.add_field(
                name=f"Order #{id}", value=f"**Items:**  {items}\n**Customer:**  {customer}\n**Type:**  {type}\n**Author:**  {author}", inline=False)

        await message.channel.send(embed=embed)

    elif param == "remove":
        if message.channel.id != __orders_channel__:
            await message.channel.send(
                embed=Embed(
                    title="Error",
                    description="This command can only be used in the orders channel.",

                    colour=__EMBED_COLOUR__
                )
            )

            return
        try:
            id = args[2]
        except IndexError:
            await message.channel.send(
                embed=Embed(
                    title="Error - No Id",
                    description="Please enter a valid id.",

                    color=__EMBED_COLOUR__,
                )
            )

            return

        # remove the order from the database with the id
        column.delete_one({"Id": int(id)})
        await message.channel.send("Order removed.")
        await message.channel.purge(limit=100)
