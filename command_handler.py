from commands import checktimers, timer, getrecipe, getcost, seedcost, help, howtogrow, orders, jobs
from datetime import datetime


async def command_handler(args, cmd, message, prefix, discord, timers, timer_index, client):
    # bootleggar shit

    dateTimeObj = datetime.now()
    timestampStr = dateTimeObj.strftime("%d-%b-%Y %H:%M:%S.%f")
    print(f"[{timestampStr}]  {message.author.name}#{message.author.discriminator} used {cmd}")
    if cmd[0] == prefix:
        await message.delete()

    if cmd == prefix + "startmash":
        await timer.tr(message, args, cmd, 6000, "Mash", timers, timer_index)
        return

    elif cmd == prefix + "startalcohol":
        await timer.tr(message, args, cmd, 3000, "Alcohol", timers, timer_index)
        return

    elif cmd == prefix + "startshine":
        await timer.tr(message, args, cmd, 6000, "Shine", timers, timer_index)
        return

    elif cmd == prefix + "checktimers":
        await checktimers.ct(cmd, message, args, timers, discord.Embed)
    elif cmd == prefix + "getrecipe":
        await getrecipe.gr(args, message, cmd, discord.Embed)

    elif cmd == prefix + "getcost":
        await getcost.gc(args, message, cmd, discord.Embed)

    # farming shit
    elif cmd == prefix + "seedcost":
        await seedcost.sc(message, args, cmd, discord.Embed)

    # general shit
    elif cmd == prefix + "help":
        await help.hp(message, discord.Embed)

    elif cmd == prefix + "howtogrow" or cmd == prefix + "h2g":
        await howtogrow.h2g(message, args, cmd)

    elif cmd == prefix + "orders":
        await orders.order(message, args, cmd, discord.Embed, client)

    elif cmd == prefix + "jobs":
        await jobs.job(message, args, cmd, discord.Embed, client)
