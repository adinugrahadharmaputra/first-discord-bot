import discord
from discord.ext import commands

client = commands.Bot(command_prefix= "pa ")

@client.event
async def on_ready():
    print("Im Ready |^_^|")
    print("--------------")
@client.command()
async def hello(ctx):  
    await ctx.send("Hello, I am Proto Alpha")

client.run('OTQzNTAwNDk1NDY3NzA4NDM3.Ygz9Tw.yjtEeiDMO3gBHD2gV0hpHhC8A74')
