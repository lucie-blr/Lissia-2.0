import discord
import json
from discord.ext import commands

with open ("data.json", "r") as f:
    data = json.load(f)
    token = data["Token"]
    prefix = data["Prefix"]

client = commands.Bot(command_prefix=prefix)

@client.command()
async def ping(ctx):
    await ctx.send("pong")

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game(f'{prefix}help | Vroum vroum'))
    print(f"Logged in as {client.user}")
    data[f'morpion'] = "False"
        
    with open(f"./data.json","w") as t:
        json.dump(data,t)

client.run(token)