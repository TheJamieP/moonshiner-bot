async def h2g(message, args, cmd):
    string = """
I'm farmer Jim, this is how to grow: \n
First, you need to check what equipment you have. You should have seeds, water buckets, a hoe, and snippers. \n
Then, you need to plant your seeds. It takes 2 seeds a plant to grow a crop. You can plant them in any spot but you should do it near a water source. \n
After you plant your seeds, you need to water them, this will be indicated by the timer on the plant turning red. \n
Once the timer is gone, you can harvest the crop. You can harvest it in and receive 5 of the crop if unsnipped and 7 if snipped.  
        """
    await message.channel.send(string)
    return
