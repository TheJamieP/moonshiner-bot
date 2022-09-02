from asyncio import sleep
from time import time
from discord.utils import find


async def tr(message, args, cmd, seconds, type, timers, timer_index):
    try:
        args[0] = args[0]
        pass
    except IndexError:
        await message.channel.send(f"You need to specify a still or ask for help using {cmd} -h")
        return

    if args[0] == "-h":
        await message.channel.send(f"Usage: {cmd} <stillname> \n Example: {cmd} A")
        return
    if len(args) < 1:
        await message.channel.send("You need to specify a Still")
        return

    # ping the user after the time has passed
    role = find(lambda r: r.name == "Bootlegger", message.guild.roles)
    print(role)
    timers.insert(timer_index, [args[0], int(
        time()) + seconds, message.author.name, type])
    await message.channel.send(f"The {type} in still {args[0].upper()} will be ready in {seconds} seconds")
    await sleep(seconds)

    for timer in timers:
        time_left = int(timer[1] - int(time()))
        if time_left <= 0:
            timers.remove(timer)
            break

    await message.channel.send(f"{role.mention} still {args[0].upper()} is ready for another batch!")
