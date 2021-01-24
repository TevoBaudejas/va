import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
import os
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print("We are ready to rol out".format(client))


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('🧙🏻MAGIJOS MINISTERIJA VIRŠ MANĘS🧙'))
    
    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("/mininfo"):
        await message.channel.send("``` 
TESTUOJU```")
        
client.run(os.getenv('TOKEN'))


