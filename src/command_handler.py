from commands import checktimers, timer, getrecipe, getcost, seedcost, help


async def command_handler(args, cmd, message, prefix, discord, timers, timer_index):
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
    # bootleggar shit
    if cmd == prefix + "startmash":
        await timer.tr(message, args, cmd, 5700, "Mash", timers, timer_index)
        return

    elif cmd == prefix + "startalcohol":
        await timer.tr(message, args, cmd, 3000, "Alcohol", timers, timer_index)
        return

    elif cmd == prefix + "startshine":
        await timer.tr(message, args, cmd, 5700, "Shine", timers, timer_index)
        return

    elif cmd == prefix + "checktimers":
        await checktimers.ct(cmd, message, args, timers, discord.Embed)
    elif cmd == prefix + "getrecipe":
        await getrecipe.gr(args, message, cmd, recipies, discord.Embed)

    elif cmd == prefix + "getcost":
        await getcost.gc(args, message, cmd, discord.Embed, recipies)

    # farming shit
    elif cmd == prefix + "seedcost":
        await seedcost.sc(message, args, cmd, discord.Embed)

    # general shit
    elif cmd == prefix + "help":
        await help.hp(message, discord.Embed)
