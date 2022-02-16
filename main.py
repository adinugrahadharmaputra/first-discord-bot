from contextvars import Token
import discord
from discord.ext import commands

import json

with open("./config.json") as conf:
    configData = json.load(conf)

token = configData["Token"]
prefix = configData["Prefix"]

client = commands.Bot(command_prefix = prefix)


@client.event
async def on_ready():
    print("Im Ready |^_^|")
    print("--------------")
@client.command()
async def hello(ctx):  
    await ctx.send("Hello, I am Proto Alpha")

client.run(token)
