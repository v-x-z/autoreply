import discord  
from discord.ext import commands  

bot = commands.Bot(command_prefix='!')  

# Replace 'YOUR_FRIEND_ID' with the ID of your friend
FRIEND_ID = 1123402776630792254

@bot.event  
async def on_message(message):  
    if message.author == bot.user:  
        return  

    if message.type == discord.MessageType.default:  
        if message.content.startswith('!'):  
            await bot.process_commands(message)  
        else:  
            if bot.user.mentioned_in(message):  
                await message.channel.send('ily toz')
            elif any(user.id == FRIEND_ID for user in message.mentions):
                await message.channel.send('ily toz')

@bot.event  
async def on_ready():  
    print(f'{bot.user} has connected to Discord!')  

bot.run('MTEwNjI0NTk0MjkzMzQ1ODk1NQ.G1xMFd.Qh5EpkEy1joPWeJAUXD_099lbM5bXmzFAF4V-k', bot=False)