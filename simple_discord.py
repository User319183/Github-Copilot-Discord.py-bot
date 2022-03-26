

#import the discord module and the os module
import discord
import os
#import ext from discord
from discord.ext import commands


#create a place to store the bot token
TOKEN = ('INSERT_TOKEN_HERE')

#give the bot priviled intents to read messages
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())


#make the ping command
@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')
    
    
#run the bot
bot.run(TOKEN)
