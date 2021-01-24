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
    await client.change_presence(activity=discord.Game('MAGIJOS MINISTERIJA VIRS MANES'; 'OMG'))
   
    
    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))

@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Lorem Ipsum asdasd", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")
    embed.set_thumbnail(url="https://pluralsight.imgix.net/paths/python-7be70baaac.png")

client.run(os.getenv('TOKEN'))


