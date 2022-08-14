
from time import time


async def ct(cmd, message, args, timers, Embed):
    embed = Embed(
        title="Timers", description="", colour=000000)
    if timers != []:
        for timer in timers:
            # structure of timer: [still, time, userid, type]
            still = timer[0]
            time_left = int(timer[1] - time())
            user = timer[2]
            type = timer[3]
            embed.add_field(
                name=f"Still: {still} - {type} - Started by {user}", value=f"Time Left: {time_left}", inline=False)

    else:
        embed.add_field(
            name="No timers", value="There are no timers currently active", inline=False)

    await message.channel.send(embed=embed)
    return
