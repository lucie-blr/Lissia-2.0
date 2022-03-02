import discord
import json
from discord.ext import commands
import os

with open ("data.json", "r") as f:
    data = json.load(f)
    token = data["Token"]
    prefix = data["Prefix"]

client = commands.Bot(command_prefix=prefix)

#Launch

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game(f'{prefix}help | Vroum vroum'))
    print(f"Logged in as {client.user}")
    data[f'morpion'] = "False"
        
    with open(f"./data.json","w") as t:
        json.dump(data,t)

#Load

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

@client.command()
@commands.has_permissions(ban_members=True)
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} command loaded.')
    print(f'{ctx.author} used load')

@load.error
async def load_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(title="Load", description="Vous n'avez pas la permission d'éxecuter cette commande.", color=discord.Color.from_rgb(17, 100, 20))
        await ctx.send(embed=embed)
        
@client.command()
@commands.has_permissions(ban_members=True)
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} command unloaded.')
    print(f'{ctx.author} used unload')

@unload.error
async def unload_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(title="Unload", description="Vous n'avez pas la permission d'éxecuter cette commande.", color=discord.Color.from_rgb(17, 100, 20))
        await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(ban_members=True)
async def reload(ctx, extension):
    if extension == "all":
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                client.unload_extension(f'cogs.{filename[:-3]}')
                await ctx.send(f'{filename[:-3]} unloaded')
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                client.load_extension(f'cogs.{filename[:-3]}')
                await ctx.send(f'{filename[:-3]} reloaded')
        print(f"{ctx.author} used reload all")
        await ctx.send("Toutes les commandes ont été reload.")
        
    else:
        print(f'{ctx.author} used reload')
        client.unload_extension(f'cogs.{    extension}')
        await ctx.send(f'{extension} command unloaded.')
        client.load_extension(f'cogs.{extension}')
        await ctx.send(f'{extension} command reloaded.')
        print(f'{ctx.author} used reload')

#commands

@client.command()
async def setprefix(ctx, prefix):
    with open (f"./data.json", "r") as f:
        data = json.load(f)
    data["Prefix"] = f"{prefix}"
    with open (f"./data.json", "w") as t:
        json.dump(data, t)
    await ctx.send(f'Prefix définie sur {prefix} au prochain redémarrage')

class NewHelpName(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()
        embed = discord.Embed(title="Help", description="Toutes les commandes du client discord", color=0x992d22)
        embed.add_field(name=f"{prefix}help", value="Affiche ce message.", inline=True)
        await destination.send(embed=embed)
client.help_command = NewHelpName()

client.run(token)