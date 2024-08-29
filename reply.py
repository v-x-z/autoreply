import discord  
from discord.ext import commands  

bot = commands.Bot(command_prefix='!')  

@bot.event  
async def on_message(message):  
    if message.author == bot.user:  
        return  

    if message.type == discord.MessageType.default:  
        if message.content.startswith('!'):  
            await bot.process_commands(message)  
        else:  
            if bot.user.mentioned_in(message):  
                await message.channel.send('your_reply_here') # this is the reply you want people to see

@bot.event  
async def on_ready():  
    print(f'{bot.user} your autoreplying has started!')

bot.run('YOUR_TOKEN', bot=False) # your discord token goes here in 'your_token' if you dont know how to get your token search up a guide 
