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
                await message.channel.send('your_reply_here') # your reply goes here to respond to people

@bot.event  
async def on_ready():  
    print(f'{bot.user} has connected to Discord!')  # you can change this to anything you want to appear in the terminal

bot.run('YOUR_TOKEN', bot=False) # discord token goes here
